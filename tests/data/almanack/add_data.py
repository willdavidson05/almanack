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
from add_entropy import add_entropy

# Initialize git repository, and add baseline code
subprocess.run(["git", "init"], check=True)
baseline_text = "Baseline content\n"
md_files = ["high_entropy/high_entropy.md", "low_entropy/low_entropy.md"]

os.makedirs("high_entropy", exist_ok=True)
os.makedirs("low_entropy", exist_ok=True)

# Adding baseline content to each Markdown file
for i in md_files:
    with open(i, "w") as f:
        f.write(baseline_text)
subprocess.run(["git", "add"] + md_files)
subprocess.run(["git", "commit", "-m", "Initial commit with baseline content"])

# Running the add_entropy.py script
add_entropy()
subprocess.run(["git", "add"] + md_files)
subprocess.run(["git", "commit", "-m", "Add entropy to Markdown files"])

def zip_md_files(file_paths, output_zip_path):
    """
    Create a zip file containing multiple markdown files.

    Args:
        file_paths: List of paths to the markdown files.
        output_zip_path: Path to the output zip file.
    """
    with zipfile.ZipFile(output_zip_path, "w") as zipf:
        for file_path in file_paths:
            zipf.write(file_path, os.path.basename(file_path))

# Zip the high_entropy and low_entropy folders separately
zip_md_files(["high_entropy/high_entropy.md"], "high_entropy.zip")
zip_md_files(["low_entropy/low_entropy.md"], "low_entropy.zip")
