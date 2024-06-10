"""
This script initlaizes a git repo, baseline content is added to Markdown files, then entropy is introduced through the 'add_entropy.py' script, and the resulting files are zipped.

Assumptions:
- The script expects 'high_entropy' and 'low_entropy' subdirectories in the execution directory.
- 'add_entropy.py' is available and responsible for introducing entropy.
- The high and low entropy files are located at 'high_entropy/high_entropy.md' and 'low_entropy/low_entropy.md' respectively.

References:
- The 'add_entropy.py' script defines the specific content changes for entropy introduction.
"""
import os
import subprocess
import zipfile

# Initialize git repository and add baseline content
subprocess.run(["git", "init"], check=True)
baseline_text = "Baseline content\n"
md_files = ["high_entropy/high_entropy.md", "low_entropy/low_entropy.md"]

for md_file in md_files:
    os.makedirs(os.path.dirname(md_file), exist_ok=True)
    with open(md_file, "w") as f:
        f.write(baseline_text)

# Running the add_entropy.py script
exec(open("add_entropy.py").read())

# Ensure that .git folders are present
subprocess.run(["git", "init", "high_entropy"], check=True)
subprocess.run(["git", "init", "low_entropy"], check=True)

# Zip the .git folders
def zip_git_folder(folder_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, "w") as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

# Zip the .git folders separately
zip_git_folder("high_entropy/.git", "high_entropy_git.zip")
zip_git_folder("low_entropy/.git", "low_entropy_git.zip")
