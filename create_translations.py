import os
import re

# Ask for input file path
input_path = input("Path to: ").strip()

# Read the translations.txt file
with open(input_path, 'r') as f:
    content = f.read()

# Find all code blocks matching the pattern
pattern = r'(UI_[A-Z]+ = \{[^}]*\})'
blocks = re.findall(pattern, content, re.DOTALL)

# Create directories and files
for block in blocks:
    # Extract the language code from the block
    match = re.search(r'UI_([A-Z]+) =', block)
    if match:
        lang_code = match.group(1)

        # Create directory in the same path as input file
        output_dir = os.path.join(os.path.dirname(input_path), lang_code)
        os.makedirs(output_dir, exist_ok=True)

        # Create file with the block content
        filename = os.path.join(output_dir, f"UI_{lang_code}.txt")
        with open(filename, 'w') as f:
            f.write(block)
