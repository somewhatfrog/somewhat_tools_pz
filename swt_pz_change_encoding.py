import os

# ask for path
while True:
    directory = input("Path to: ").strip()
    if os.path.exists(directory):
        break
    else:
        print("No such dir")

# ask for build version
build = input("Build: ").strip()

# encoding maps
encoding_map_41 = {
    "UI_AR.txt": "cp1252",
    "UI_CA.txt": "iso-8859-15",
    "UI_CH.txt": "utf-8",
    "UI_CN.txt": "utf-8",
    "UI_CS.txt": "cp1250",
    "UI_DA.txt": "cp1252",
    "UI_DE.txt": "cp1252",
    "UI_EN.txt": "utf-8",
    "UI_ES.txt": "cp1252",
    "UI_FI.txt": "cp1252",
    "UI_FR.txt": "cp1252",
    "UI_HU.txt": "cp1250",
    "UI_ID.txt": "utf-8",
    "UI_IT.txt": "cp1252",
    "UI_JP.txt": "utf-8",
    "UI_KO.txt": "utf-16",
    "UI_NL.txt": "cp1252",
    "UI_NO.txt": "cp1252",
    "UI_PH.txt": "utf-8",
    "UI_PL.txt": "cp1250",
    "UI_PT.txt": "cp1252",
    "UI_PTBR.txt": "cp1252",
    "UI_RO.txt": "utf-8",
    "UI_RU.txt": "cp1251",
    "UI_TH.txt": "utf-8",
    "UI_TR.txt": "cp1254",
    "UI_UA.txt": "cp1251"
}
encoding_map_42 = {
    "UI_AR.txt": "cp1252",
    "UI_CA.txt": "iso-8859-15",
    "UI_CH.txt": "utf-8",
    "UI_CN.txt": "utf-8",
    "UI_CS.txt": "cp1250",
    "UI_DA.txt": "utf-8",
    "UI_DE.txt": "utf-8",
    "UI_EN.txt": "utf-8",
    "UI_ES.txt": "utf-8",
    "UI_FI.txt": "utf-8",
    "UI_FR.txt": "utf-8",
    "UI_HU.txt": "utf-8",
    "UI_ID.txt": "utf-8",
    "UI_IT.txt": "utf-8",
    "UI_JP.txt": "utf-8",
    "UI_KO.txt": "utf-16",
    "UI_NL.txt": "utf-8",
    "UI_NO.txt": "utf-8",
    "UI_PH.txt": "utf-8",
    "UI_PL.txt": "utf-8",
    "UI_PT.txt": "utf-8",
    "UI_PTBR.txt": "utf-8",
    "UI_RO.txt": "utf-8",
    "UI_RU.txt": "utf-8",
    "UI_TH.txt": "utf-8",
    "UI_TR.txt": "utf-8",
    "UI_UA.txt": "utf-8"
}

if build == "41":
    encoding_map = encoding_map_41
elif build == "42":
    encoding_map = encoding_map_42
else:
    print("Unknown build version")
    exit()

def convert_encoding(file_path, target_encoding):
    try:
        # create backup file
        backup_path = file_path + "_UTF-8"
        with open(file_path, 'r', encoding='utf-8') as source:
            with open(backup_path, 'w', encoding='utf-8') as backup:
                backup.write(source.read())
        print(f"Backup: {backup_path}")

        # read file as UTF-8 and write with target encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # write file with target encoding
        with open(file_path, 'w', encoding=target_encoding) as f:
            f.write(content)

        print(f"Converted {file_path} to {target_encoding}")

    except Exception as e:
        print(f"Error {file_path}: {e}")

# process all matching files in the specified directory and subdirectories
for filename, target_encoding in encoding_map.items():
    # find all files with this name in the specified directory and subdirectories
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                convert_encoding(file_path, target_encoding)

print("Done")
