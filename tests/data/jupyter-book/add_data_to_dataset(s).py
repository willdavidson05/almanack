from zipfile import ZipFile

# Name of zip contaitng .md files
filename = "test_data.zip"

# List of .md files
md_filenames = ["high_entropy.md","low_entropy.md"]

# Content to add to .md files
data_to_add = "\n## New Section\n Adding in desired content to markdown file"

def update_md_files(zip_path,md_files,data):
    '''
    Function to update specified markdown files in the zip archive.
    
    Args:
        - zip_path (str): Path to the zip file.
        - md_files (list): List of markdown file names to be updated.
        - data (str): Content to be added to the markdown files.
    '''
    with ZipFile(zip_path,'w') as zip:
        for i in md_files:
            # open the markdown file in the zip and write the new data 
            with zip.open(i,'w') as md_file:
                md_file.write(data.encode())

# Select which file(s) to update
print("Which Markdown file(s) do you want to update?")
print("1. high_entropy.md")
print("2. low_entropy.md")
print("3. Both")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    files_to_update = ["high_entropy.md"]
elif choice == "2":
    files_to_update = ["low_entropy.md"]
elif choice == "3":
    files_to_update = md_filenames
else:
    print("Invalid choice. Exiting.")
    exit()

# Update the selected markdown files
update_md_files(filename, files_to_update, data_to_add)

print("Update complete.")
