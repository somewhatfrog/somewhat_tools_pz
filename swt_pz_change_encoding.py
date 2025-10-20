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
    "_AR.txt": "cp1252",
    "_CA.txt": "iso-8859-15",
    "_CH.txt": "utf-8",
    "_CN.txt": "utf-8",
    "_CS.txt": "cp1250",
    "_DA.txt": "cp1252",
    "_DE.txt": "cp1252",
    "_EN.txt": "utf-8",
    "_ES.txt": "cp1252",
    "_FI.txt": "cp1252",
    "_FR.txt": "cp1252",
    "_HU.txt": "cp1250",
    "_ID.txt": "utf-8",
    "_IT.txt": "cp1252",
    "_JP.txt": "utf-8",
    "_KO.txt": "utf-16",
    "_NL.txt": "cp1252",
    "_NO.txt": "cp1252",
    "_PH.txt": "utf-8",
    "_PL.txt": "cp1250",
    "_PT.txt": "cp1252",
    "_PTBR.txt": "cp1252",
    "_RO.txt": "utf-8",
    "_RU.txt": "cp1251",
    "_TH.txt": "utf-8",
    "_TR.txt": "cp1254",
    "_UA.txt": "cp1251"
}
encoding_map_42 = {
    "_AR.txt": "cp1252",
    "_CA.txt": "iso-8859-15",
    "_CH.txt": "utf-8",
    "_CN.txt": "utf-8",
    "_CS.txt": "cp1250",
    "_DA.txt": "utf-8",
    "_DE.txt": "utf-8",
    "_EN.txt": "utf-8",
    "_ES.txt": "utf-8",
    "_FI.txt": "utf-8",
    "_FR.txt": "utf-8",
    "_HU.txt": "utf-8",
    "_ID.txt": "utf-8",
    "_IT.txt": "utf-8",
    "_JP.txt": "utf-8",
    "_KO.txt": "utf-16",
    "_NL.txt": "utf-8",
    "_NO.txt": "utf-8",
    "_PH.txt": "utf-8",
    "_PL.txt": "utf-8",
    "_PT.txt": "utf-8",
    "_PTBR.txt": "utf-8",
    "_RO.txt": "utf-8",
    "_RU.txt": "utf-8",
    "_TH.txt": "utf-8",
    "_TR.txt": "utf-8",
    "_UA.txt": "utf-8"
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
for root, dirs, files in os.walk(directory):
    for filename in files:
        # check if any key from encoding_map is in the filename
        for key, target_encoding in encoding_map.items():
            if key in filename:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    convert_encoding(file_path, target_encoding)

print("Done")
