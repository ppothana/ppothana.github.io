import csv
import os

# Define the output directory for .md files
output_dir = "../_publications"
os.makedirs(output_dir, exist_ok=True)

# Read the CSV file
with open("../citations.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Debugging: Print the keys to verify
        print(row.keys())

        # Generate the filename based on the title and year
        title_slug = row["Title"].lower().replace(" ", "-").replace(",", "").replace(":", "").replace("&", "and")
        filename = f"{row['Year']}-{title_slug}.md"
        filepath = os.path.join(output_dir, filename)

        # Create the .md file content
        content = f"""---
title: "{row['Title']}"
authors: "{row.get('Authors', 'Unknown')}"  # Handle missing 'Authors' key
collection: publications
category: manuscripts
date: {row['Year']}-01-01
venue: "{row.get('Publication', 'Unknown')}"  # Handle missing 'Publication' key
volume: "{row.get('Volume', '')}"
number: "{row.get('Number', '')}"
pages: "{row.get('Pages', '')}"
publisher: "{row.get('Publisher', '')}"
excerpt: "This is a placeholder excerpt for the publication titled '{row['Title']}'."
---

This is the detailed description of the publication titled **"{row['Title']}"**. You can add more information here.
"""
        # Write the content to the .md file
        with open(filepath, "w", encoding="utf-8") as mdfile:
            mdfile.write(content)

print(f"Markdown files generated in '{output_dir}' directory.")