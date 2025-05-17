import os  # To work with files and directories
import shutil  # To move files

# Folder where your files are (change this to your folder path)
target_folder = "."  # "." means current directory

# Create a dictionary to map file extensions to folder names
file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Code': ['.py', '.cpp', '.js', '.html', '.css'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Archives': ['.zip', '.rar', '.tar']
}

# Loop through all the files in the folder
for file_name in os.listdir(target_folder):
    file_path = os.path.join(target_folder, file_name)

    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file_name)

    # Check what category the file belongs to
    moved = False
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            folder_path = os.path.join(target_folder, folder)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file
            shutil.move(file_path, os.path.join(folder_path, file_name))
            print(f"Moved '{file_name}' to '{folder}/'")
            moved = True
            break

    # If the file type is unknown, move to "Others"
    if not moved:
        others_path = os.path.join(target_folder, "Others")
        if not os.path.exists(others_path):
            os.makedirs(others_path)
        shutil.move(file_path, os.path.join(others_path, file_name))
        print(f"Moved '{file_name}' to 'Others/'")
