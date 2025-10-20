**swt_pz_create_translation_files** - takes the file with llm output (or whatever you're going to use) piled with translation blocks it spat out and creates dirs and files for each translation blocks next to the input file

Usage:
1. Path to file: /file_with_translations_to_all_languages.* (any text format, yaml, etc)
2. Block type: ContextMenu
3. Creates: /LANG/ContextMenu_LANG.txt 

**swt_pz_change_encoding** - takes path and changes the encoding of all translation files to a specified game version ahd creates backups (it expects UTF-8 as source and i hope your sources are UTF-8 kek)

Usage:
1. Path to directory: /42/media/lua/shared/Translations
2. Build: 42
