# Photo Renaming Script

This Python script renames photo files in a specified input folder and copies them to an output folder. The new filenames follow the format "character_<random unique ID>". The unique ID is an 8-character alphanumeric string. Optionally, the script can also delete the original files after successful renaming and copying.

## Features
- Renames photo files with a unique 8-character alphanumeric ID.
- Copies renamed files to an output folder.
- Optionally deletes the original files after renaming.

## Requirements
- Python 3.x
- No additional libraries required

## Setup
1. Create two folders named `Images_to_Rename` and `Renamed_Images` in the same directory as the script.
2. Place the photo files you want to rename in the `Images_to_Rename` folder.

## Usage
1. Ensure you have Python 3 installed on your system.
2. Save the script as `rename_photos.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command:
   ```bash
   python rename_photos.py