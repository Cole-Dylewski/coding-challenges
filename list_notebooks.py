import os
import re

# Paths
README_FILE = "README.md"
CHALLENGES_DIR = "Coding Challenges"

def get_notebooks():
    """
    Scan the Coding Challenges/ folder for all .ipynb files.
    """
    notebooks = []
    for root, _, files in os.walk(CHALLENGES_DIR):
        for f in files:
            if f.endswith(".ipynb"):
                notebooks.append(f)
    return sorted(notebooks)

def generate_table(notebooks):
    """
    Generate a Markdown table for the README with notebook links and placeholder descriptions.
    """
    table = "| Notebook | Description |\n|----------|-------------|\n"
    for nb in notebooks:
        # Default placeholder description for new notebooks
        desc = "Challenge description to be added."
        
        # Special handling for known notebooks
        if nb == "close_api.ipynb":
            desc = (
                "Implements **Post Body Hash generation** for secure API request signing. "
                "Covers hashing techniques (SHA256, HMAC), payload integrity validation, "
                "and automated signing for authenticated requests."
            )

        # Anchor link needs to strip periods and lowercase
        table += f"| [`{nb}`](#{nb.replace('.', '').lower()}) | {desc} |\n"
    return table

def update_readme(table):
    """
    Replace the existing table in README.md under the Challenges Overview section.
    """
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to find the section between the table header and the next '---' separator
    pattern = re.compile(r"(## 📓 Challenges Overview.*?\| Notebook.*?\n)([\s\S]*?)(?=\n---|\Z)")
    updated = pattern.sub(r"\1" + table + "\n", content)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    notebooks = get_notebooks()
    table = generate_table(notebooks)
    update_readme(table)
    print(f"✅ Updated README.md with {len(notebooks)} notebooks found.")
