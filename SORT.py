import os, shutil

desktop_path = (os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")) #Get Onedrive desktop path

if os.path.exists(desktop_path):
    pass
elif os.path.exists(os.path.join(os.path.expanduser("~"), "Desktop")):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
else:
    print("Couldnt find desktop!")
    raise FileNotFoundError("Could not find the Desktop Folder") #Raise FileNotFoundError

os.chdir(desktop_path)

def is_extension(path, exts):
    return os.path.splitext(path)[1].lower() in exts

file_paths = []

for item in os.listdir(): #Get all files/folders in desktop
    full_path = os.path.join(desktop_path, item) # Full path of every item in desktop
    if os.path.isfile(full_path) and not full_path == __file__:
        file_paths.append(full_path)

os.makedirs(os.path.join('Images'), exist_ok=True) # Make directory 'Images', if already exists then do nothing
os.makedirs(os.path.join('Media'), exist_ok=True)
os.makedirs(os.path.join('Text'), exist_ok=True)
os.makedirs(os.path.join('Media/Audio'), exist_ok=True)
os.makedirs(os.path.join('Text/Doc'), exist_ok=True)
os.makedirs(os.path.join('Coding'), exist_ok=True)

for path in file_paths: # Repeat for every item in desktop
    if is_extension(path, ['.png', '.jpg', '.jpeg', '.jfif', '.gif', '.apng', '.webp', '.ico']):
        shutil.move(path, os.path.join('Images')) # Move file to 'Images'
    elif is_extension(path, ['.mp4', '.mkv', '.flv', '.mov']):
        shutil.move(path, os.path.join('Media'))
    elif is_extension(path, ['.mp3', '.wav']):
        shutil.move(path, os.path.join('Media/Audio'))
    elif is_extension(path, ['.doc', '.docx']):
        shutil.move(path, os.path.join('Text/Doc'))
    elif is_extension(path, ['.rtf', '.txt']):
        shutil.move(path, os.path.join('Text'))
    elif is_extension(path, ['.py', '.html', '.js', '.c', '.cpp']):
        shutil.move(path, os.path.join('Coding'))
