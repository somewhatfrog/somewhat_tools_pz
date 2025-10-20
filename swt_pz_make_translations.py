import os
import re

# ask for input file path
input_path = input("Path to: ").strip()

# ask for translation type
block_type = input("Block Type: ").strip()

# read the input file
with open(input_path, 'r') as f:
    content = f.read()

# find all code blocks matching the pattern
pattern = rf'({block_type}_[A-Z]+ = \{{[^}}]*\}})'
blocks = re.findall(pattern, content, re.DOTALL)

# create directories and files
for block in blocks:
    # extract translation blocks
    match = re.search(rf'{block_type}_([A-Z]+) =', block)
    if match:
        lang_code = match.group(1)

        # create directory
        output_dir = os.path.join(os.path.dirname(input_path), lang_code)
        os.makedirs(output_dir, exist_ok=True)

        # create file
        filename = os.path.join(output_dir, f"{block_type}_{lang_code}.txt")
        with open(filename, 'w') as f:
            f.write(block)

print("Done")
