import os
import shutil

# Enter folder path to organize
path = input("Enter folder path: ")

# File extensions
images = [".jpg", ".jpeg", ".png", ".gif"]
documents = [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"]
videos = [".mp4", ".avi", ".mkv", ".mov"]

# Create folders automatically
os.makedirs(os.path.join(path, "Images"), exist_ok=True)
os.makedirs(os.path.join(path, "Documents"), exist_ok=True)
os.makedirs(os.path.join(path, "Videos"), exist_ok=True)
os.makedirs(os.path.join(path, "Others"), exist_ok=True)

# Organize files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        if extension in images:
            shutil.move(file_path, os.path.join(path, "Images", file))

        elif extension in documents:
            shutil.move(file_path, os.path.join(path, "Documents", file))

        elif extension in videos:
            shutil.move(file_path, os.path.join(path, "Videos", file))

        else:
            shutil.move(file_path, os.path.join(path, "Others", file))

print("Files organized successfully!")
