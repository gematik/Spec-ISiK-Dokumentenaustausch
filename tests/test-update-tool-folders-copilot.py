import unittest
import os
import shutil
import tempfile
from unittest.mock import patch
from update_tool_folders import update_folders

class TestUpdateToolFolders(unittest.TestCase):

    def setUp(self):
        self.folders = ["test_folder"]
        self.exclude_files = ["config.yaml"]
        self.base_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.base_dir, "test_folder"), exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.base_dir, ignore_errors=True)

    def create_file(self, directory, filename, content="test content"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as f:
            f.write(content)
        return file_path

    @patch("update_tool_folders.clone_source_repo")
    @patch("update_tool_folders.copy_folders")
    def test_no_additional_files_overwritten(self, mock_copy_folders, mock_clone_source_repo):
        mock_clone_source_repo.return_value = None
        mock_copy_folders.return_value = None

        update_folders(self.folders, exclude_files=[])

        mock_clone_source_repo.assert_called_once()
        mock_copy_folders.assert_called_once_with(mock_clone_source_repo.return_value, self.folders, [])

    @patch("update_tool_folders.clone_source_repo")
    @patch("update_tool_folders.copy_folders")
    def test_excluded_files_not_overwritten(self, mock_copy_folders, mock_clone_source_repo):
        mock_clone_source_repo.return_value = None
        mock_copy_folders.return_value = None

        update_folders(self.folders, exclude_files=self.exclude_files)

        mock_clone_source_repo.assert_called_once()
        mock_copy_folders.assert_called_once_with(mock_clone_source_repo.return_value, self.folders, self.exclude_files)

    @patch("update_tool_folders.clone_source_repo")
    @patch("update_tool_folders.copy_folders")
    def test_common_files_overwritten(self, mock_copy_folders, mock_clone_source_repo):
        mock_clone_source_repo.return_value = None
        mock_copy_folders.return_value = None

        update_folders(self.folders, exclude_files=[])

        mock_clone_source_repo.assert_called_once()
        mock_copy_folders.assert_called_once_with(mock_clone_source_repo.return_value, self.folders, [])

    @patch("update_tool_folders.clone_source_repo")
    @patch("update_tool_folders.copy_folders")
    def test_no_folders_to_update(self, mock_copy_folders, mock_clone_source_repo):
        mock_clone_source_repo.return_value = None
        mock_copy_folders.return_value = None

        update_folders([], exclude_files=[])

        mock_clone_source_repo.assert_called_once()
        mock_copy_folders.assert_not_called()

    @patch("update_tool_folders.clone_source_repo")
    @patch("update_tool_folders.copy_folders")
    def test_missing_folder_in_source_repo(self, mock_copy_folders, mock_clone_source_repo):
        mock_clone_source_repo.return_value = None
        mock_copy_folders.return_value = None

        update_folders(["nonexistent_folder"], exclude_files=[])

        mock_clone_source_repo.assert_called_once()
        mock_copy_folders.assert_called_once_with(mock_clone_source_repo.return_value, ["nonexistent_folder"], [])

if __name__ == '__main__':
    unittest.main()
