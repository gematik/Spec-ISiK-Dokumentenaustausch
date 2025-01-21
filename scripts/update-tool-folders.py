import os
import shutil
import tempfile
import subprocess

# This script updates the specified folders in the current repository with the contents of the specified source repository and branch. 
# It is intended for local use and the files must be added and committed manually after running the script. 

# Define the source repository and branch
SOURCE_REPO = "https://github.com/gematik/spec-ISiK-Basismodul"
SOURCE_BRANCH = "main-isik-stufe-4"

# Define the list of folders to update
FOLDERS = [".github", "scripts"]

# Define the list of files to exclude from updating
EXCLUDE_FILES = ["scripts/config.yaml"]

def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
    return result

def clone_source_repo(temp_dir):
    run_command(f"git clone --branch {SOURCE_BRANCH} {SOURCE_REPO} {temp_dir}")
#TODO get the folder directly, since git command has low performance 

def copy_folders(temp_dir, folders, exclude_files):
    for folder in folders:
        src_folder = os.path.join(temp_dir, folder)
        if os.path.exists(src_folder):
            dest_folder = os.path.join(os.getcwd(), folder)
            if os.path.exists(dest_folder):
                shutil.rmtree(dest_folder)
            shutil.copytree(src_folder, dest_folder, ignore=shutil.ignore_patterns(*exclude_files))
        else:
            print(f"Folder {folder} does not exist in the source repository.")

def update_folders(folders, exclude_files):
    print("Updating folders...")
    with tempfile.TemporaryDirectory() as temp_dir:
        clone_source_repo(temp_dir)
        copy_folders(temp_dir, folders, exclude_files)
    print("Update complete.")

def main():
    update_folders(FOLDERS, EXCLUDE_FILES)

if __name__ == "__main__":
    main()
