import os
import shutil

# Define the relative path to the folder to be organized
script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, 'organzie_files')
print (folder_path)

# Define subfolder names for each file type
subfolders = {
    'images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
    'archives': ['.zip', '.rar', '.tar', '.gz', '.7z']
}

# Create subfolders if they do not exist
for subfolder in subfolders.keys():
    os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)

# Move files into respective subfolders based on their extensions
for file_name in os.listdir(folder_path):
    # Skip directories
    if os.path.isdir(os.path.join(folder_path, file_name)):
        continue
    
    file_ext = os.path.splitext(file_name)[1].lower()
    moved = False
    
    for subfolder, extensions in subfolders.items():
        if file_ext in extensions:
            shutil.move(os.path.join(folder_path, file_name), os.path.join(folder_path, subfolder, file_name))
            print(os.path.join(folder_path, file_name), os.path.join(folder_path, subfolder, file_name))
            moved = True
            break

    # Handle files with unknown extensions
    if not moved:
        other_folder = os.path.join(folder_path, 'other')
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(os.path.join(folder_path, file_name), os.path.join(other_folder, file_name))
        
print("Files organized successfully.")
