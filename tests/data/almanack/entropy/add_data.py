"""
This script initializes a Git repository, adds baseline content to Markdown files,
introduces entropy through the 'add_entropy.py' script, and zips the resulting
files .git directories.

Functions:
- `zip_git_folder(folder_path, output_zip_path)`: Takes in a folder path, performs a zip on that folder, and outputs a zip file.

References:
- The 'add_entropy.py' script defines the specific content changes for entropy introduction.

Command-Line Instructions:
- To unzip the created zip files and view the contents, use the following commands:
  unzip high_entropy_git.zip -d high_entropy_unzipped
  unzip low_entropy_git.zip -d low_entropy_unzipped
"""

import os
import subprocess
import zipfile

from add_entropy import add_entropy


def zip_git_folder(folder_path, output_zip_path):
    """
    Creates a zip file containing the contents of a folder.

    Args:
        folder_path (str): The path to the folder to be zipped.
        output_zip_path (str): The path to the output zip file.
    """
    with zipfile.ZipFile(output_zip_path, "w") as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


def main():
    # Initialize git repository and add baseline content
    subprocess.run(["git", "init"], check=True)
    baseline_text = "Baseline content\n"
    md_files = ["high_entropy/high_entropy.md", "low_entropy/low_entropy.md"]

    for md_file in md_files:
        os.makedirs(os.path.dirname(md_file), exist_ok=True)
        with open(md_file, "w") as f:
            f.write(baseline_text)

    # Run the add_entropy.py script
    add_entropy()

    # Ensure that .git folders are present
    subprocess.run(["git", "init", "high_entropy"], check=True)
    subprocess.run(["git", "init", "low_entropy"], check=True)

    # Zip the .git folders separately
    zip_git_folder("high_entropy/.git", "high_entropy_git.zip")
    zip_git_folder("low_entropy/.git", "low_entropy_git.zip")


if __name__ == "__main__":
    main()
