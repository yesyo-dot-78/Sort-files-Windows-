import os, shutil

desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop") #Get Onedrive desktop path

if os.path.exists(desktop_path):
    pass
elif os.path.exists(os.path.join(os.path.expanduser("~"), "Desktop")):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
else:
    print("Couldnt find desktop!")
    raise FileNotFoundError("Could not find the Desktop Folder") #Raise FileNotFoundError

def is_extension(path, exts):
    return os.path.splitext(path)[1].lower() in exts

file_paths = []

for item in os.listdir(desktop_path): #Get all files/folders in desktop
    full_path = os.path.join(desktop_path, item) # Full path of every item in desktop
    if os.path.isfile(full_path) and not full_path == __file__:
        file_paths.append(full_path)

os.makedirs(os.path.join(desktop_path, 'Images'), exist_ok=True) # Make directory 'Images', if already exists then do nothing
os.makedirs(os.path.join(desktop_path, 'Media'), exist_ok=True)
os.makedirs(os.path.join(desktop_path, 'Text'), exist_ok=True)
os.makedirs(os.path.join(desktop_path, 'Media/Audio'), exist_ok=True)
os.makedirs(os.path.join(desktop_path, 'Text/Doc'), exist_ok=True)
os.makedirs(os.path.join(desktop_path, 'Coding'), exist_ok=True)

for path in file_paths: # Repeat for every item in desktop
    if is_extension(path, ['.png', '.jpg', '.jpeg', '.jfif', '.gif', '.apng', '.webp', '.ico']):
        shutil.move(path, os.path.join(desktop_path, 'Images')) # Move file to 'Images'
    elif is_extension(path, ['.mp4', '.mkv', '.flv', '.mov']):
        shutil.move(path, os.path.join(desktop_path, 'Media'))
    elif is_extension(path, ['.mp3', '.wav']):
        shutil.move(path, os.path.join(desktop_path, 'Media/Audio'))
    elif is_extension(path, ['.doc', '.docx']):
        shutil.move(path, os.path.join(desktop_path, 'Text/Doc'))
    elif is_extension(path, ['.rtf', '.txt']):
        shutil.move(path, os.path.join(desktop_path, 'Text'))
    elif is_extension(path, ['.py', '.html', '.js', '.c', '.cpp']):
        shutil.move(path, os.path.join(desktop_path, 'Coding'))
