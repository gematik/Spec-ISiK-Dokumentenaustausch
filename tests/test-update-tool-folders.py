import unittest
from unittest.mock import patch, call
import subprocess
import update_tool_folders

class TestUpdateToolFolders(unittest.TestCase):

    @patch('update_tool_folders.subprocess.run')
    def test_run_command_success(self, mock_run):
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "success"
        result = update_tool_folders.run_command("echo success")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "success")
        mock_run.assert_called_once_with("echo success", shell=True, cwd=None, capture_output=True, text=True)

    @patch('update_tool_folders.subprocess.run')
    def test_run_command_failure(self, mock_run):
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "error"
        result = update_tool_folders.run_command("echo error")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, "error")
        mock_run.assert_called_once_with("echo error", shell=True, cwd=None, capture_output=True, text=True)

    @patch('update_tool_folders.run_command')
    def test_get_current_branch(self, mock_run_command):
        mock_run_command.return_value.stdout = "main"
        current_branch = update_tool_folders.get_current_branch()
        self.assertEqual(current_branch, "main")
        mock_run_command.assert_called_once_with("git branch --show-current")

    @patch('update_tool_folders.run_command')
    def test_update_folders(self, mock_run_command):
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

if __name__ == "__main__":
    unittest.main()