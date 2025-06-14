import os
import bibtexparser

BIB_FILE = '../data/publications.bib'
OUTPUT_DIR = '../_publications'

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(BIB_FILE, 'r') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for entry in bib_database.entries:
    entry_id = entry.get('ID', 'entry')
    file_path = os.path.join(OUTPUT_DIR, f"{entry_id}.md")
    
    front_matter = "---\n"
    front_matter += "layout: publication\n"
    front_matter += f"title: \"{entry.get('title', 'No Title')}\"\n"
    front_matter += f"authors: \"{entry.get('author', 'Unknown')}\"\n"
    if 'year' in entry:
        front_matter += f"date: \"{entry.get('year')}-01-01\"\n"
    else:
        front_matter += "date: \"1900-01-01\"\n"
    front_matter += "bibtex: |\n"
    for key, value in entry.items():
        front_matter += f"  {key}: {value}\n"
    front_matter += "---\n\n"
    
    content = f"## {entry.get('title', 'No Title')}\n\n"
    content += f"**Authors:** {entry.get('author', 'Unknown')}\n\n"
    content += f"**Year:** {entry.get('year', 'N/A')}\n\n"
    content += "Citation details are provided in the bibtex block above.\n"
    
    with open(file_path, 'w') as md_file:
        md_file.write(front_matter + content)