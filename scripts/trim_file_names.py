import os

# Define the path to the _publications folder
publications_folder = "../_publications"

# Iterate through all files in the folder
for filename in os.listdir(publications_folder):
    # Check if the file is a markdown file
    if filename.endswith(".md"):
        # Trim the filename to the first 20 characters and append .md
        new_filename = filename[:20] + ".md"
        # Rename the file
        os.rename(
            os.path.join(publications_folder, filename),
            os.path.join(publications_folder, new_filename)
        )

print("File names trimmed successfully!")