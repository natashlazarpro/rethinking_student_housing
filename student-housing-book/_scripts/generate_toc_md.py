"""
To run this: 
python3 student-housing-book/_scripts/generate_toc_md.py
"""

from pathlib import Path
import yaml

def generate_toc_md(toc_yaml_path: Path, output_md_path: Path):
    with open(output_md_path, 'w') as md_file:
        md_file.write("# Table of Contents\n\n")
        with open(toc_yaml_path, 'r') as file:
            toc_data = yaml.safe_load(file)
        for p in toc_data['parts']:
            part_title = p['caption']
            md_file.write(f"## {part_title}\n\n")
            for chapter in p.get('chapters', []):
                file_name = chapter['file']
                title = file_name.split("/")[-1].replace('_', ' ').replace('.md', '').title()
                md_file.write(f"[{title}]({file_name})\n\n")

if __name__ == "__main__":
    toc_yaml = Path('student-housing-book/_toc.yml')
    output_md = Path('student-housing-book/markdowns/0.2_table_of_contens.md')
    generate_toc_md(toc_yaml, output_md)