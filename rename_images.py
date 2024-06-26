import os
import random
import string
import shutil

def generate_unique_id(length=8):
    # Generates a random unique ID of specified length
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def rename_photos(input_directory, output_directory, prefix=""):
    # List all files in the input directory
    files = os.listdir(input_directory)

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in files:
        # Check if the file is a photo based on its extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            # Generate a unique ID
            unique_id = generate_unique_id()
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            # Construct the new filename
            new_filename = f"{prefix}{unique_id}{file_extension}"
            # Get the full paths for the old and new filenames
            old_file = os.path.join(input_directory, filename)
            new_file = os.path.join(output_directory, new_filename)
            # Copy the file to the new location with the new name
            shutil.copy(old_file, new_file)
            print(f"Copied and renamed '{filename}' to '{new_filename}'")

    # Ask the user if they want to delete the contents of the input directory
    if all(filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')) for filename in files):
        delete_contents = input("Do you want to delete the contents of the 'Images_to_Rename' folder? (yes/no): ").strip().lower()
        if delete_contents == 'yes':
            for filename in files:
                os.remove(os.path.join(input_directory, filename))
            print(f"All files in '{input_directory}' have been deleted.")
        else:
            print("The files in 'Images_to_Rename' have not been deleted.")

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define input and output directories
input_directory = os.path.join(script_directory, 'Images_to_Rename')
output_directory = os.path.join(script_directory, 'Renamed_Images')

# Ask the user for a prefix
prefix = input("Enter a prefix for the filenames (press enter for no prefix): ").strip()
if prefix:
    prefix += "_"  # Add an underscore after the prefix if provided

# Run the rename function
rename_photos(input_directory, output_directory, prefix)