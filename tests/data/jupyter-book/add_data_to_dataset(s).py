from zipfile import ZipFile

filename = "test_data.zip"
md_filenames = ["high_entropy.md","low_entropy.md"]
# Add desired data
data_to_add = "\n## New Section\n Adding in desired content to markdown file"

def update_md_files(zip_path,md_files,data):
    '''
    Updating Specified markdown files in the zip.
    '''
    with ZipFile(zip_path,'w') as zip:
        for i in md_files:
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
