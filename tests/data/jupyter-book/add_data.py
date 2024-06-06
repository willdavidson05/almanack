import os
import subprocess
import zipfile

# Initialize git repository, and add baseline code
subprocess.run(["git", "init"])
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
exec(open("add_entropy.py").read())
subprocess.run(["git", "add"] + md_files)
subprocess.run(["git", "commit", "-m", "Add entropy to Markdown files"])


def zip_md_files(file1_path, file2_path, output_zip_path):
    """
    Create a zip file containing two markdown files.

    Args:
        file1_path: Path to the first markdown file.
        file2_path: Path to the second markdown file.
        output_zip_path: Path to the output zip file.
    """
    with zipfile.ZipFile(output_zip_path, "w") as zipf:
        zipf.write(file1_path, "high_entropy.md")
        zipf.write(file2_path, "low_entropy.md")


# Zip the high_entropy and low_entropy folder
zip_md_files(
    "high_entropy/high_entropy.md", "low_entropy/low_entropy.md", "entropy_data.zip"
)
