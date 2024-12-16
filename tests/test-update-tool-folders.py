import unittest
from unittest.mock import patch, call, MagicMock
import os
import shutil
import tempfile
import subprocess
import update_tool_folders

class TestUpdateToolFolders(unittest.TestCase):

    @patch('update_tool_folders.subprocess.run')
    def test_run_command_success(self, mock_run):
        # Test that run_command works correctly when the command succeeds
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "success"
        result = update_tool_folders.run_command("echo success")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "success")
        mock_run.assert_called_once_with("echo success", shell=True, cwd=None, capture_output=True, text=True)

    @patch('update_tool_folders.subprocess.run')
    def test_run_command_failure(self, mock_run):
        # Test that run_command handles errors correctly when the command fails
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "error"
        result = update_tool_folders.run_command("echo error")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, "error")
        mock_run.assert_called_once_with("echo error", shell=True, cwd=None, capture_output=True, text=True)

    @patch('update_tool_folders.run_command')
    def test_get_current_branch(self, mock_run_command):
        # Test that get_current_branch returns the correct branch name
        mock_run_command.return_value.stdout = "main"
        current_branch = update_tool_folders.get_current_branch()
        self.assertEqual(current_branch, "main")
        mock_run_command.assert_called_once_with("git branch --show-current")

    @patch('update_tool_folders.run_command')
    def test_update_folders(self, mock_run_command):
        # Test that update_folders calls the correct git commands
        folders = ["folder1", "folder2"]
        current_branch = "main"
        update_tool_folders.update_folders(folders, current_branch)
        expected_calls = [
            call(f"git checkout {update_tool_folders.SOURCE_BRANCH}"),
            call(f"git checkout {current_branch} -- folder1"),
            call(f"git checkout {current_branch} -- folder2"),
            call(f"git checkout {current_branch}")
        ]
        mock_run_command.assert_has_calls(expected_calls, any_order=False)

    @patch('update_tool_folders.shutil.copy2')
    @patch('update_tool_folders.os.path.exists')
    @patch('update_tool_folders.os.makedirs')
    @patch('update_tool_folders.os.listdir')
    @patch('update_tool_folders.shutil.copytree')
    def test_additional_files_not_overwritten(self, mock_copytree, mock_listdir, mock_makedirs, mock_path_exists, mock_copy2):
        # Setup mocks
        mock_path_exists.side_effect = lambda path: path.endswith("dest_folder") or path.endswith("additional_file.txt")
        mock_listdir.side_effect = lambda path: ["file1.txt", "file2.txt"] if path.endswith("src_folder") else ["additional_file.txt"]
        
        temp_dir = tempfile.gettempdir()
        src_folder = os.path.join(temp_dir, "src_folder")
        dest_folder = os.path.join(os.getcwd(), "dest_folder")
        
        # Call the function
        update_tool_folders.copy_folders(temp_dir, ["src_folder"], ["file2.txt"])
        
        # Check that additional files are not overwritten
        mock_copy2.assert_called_once_with(os.path.join(src_folder, "file1.txt"), os.path.join(dest_folder, "file1.txt"))
        mock_copytree.assert_not_called()
        self.assertTrue(mock_path_exists(os.path.join(dest_folder, "additional_file.txt")))

if __name__ == "__main__":
    unittest.main()