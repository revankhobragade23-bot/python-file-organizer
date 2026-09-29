import os
import shutil

folder = input("Enter folder path: ")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".doc", ".docx", ".txt", ".odt"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

if not os.path.exists(folder):
    print("Folder not found.")
    exit()

for category in categories:
    os.makedirs(os.path.join(folder, category), exist_ok=True)

os.makedirs(os.path.join(folder, "Others"), exist_ok=True)

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()
    moved = False

    for category, extensions in categories.items():
        if extension in extensions:
            destination = os.path.join(folder, category, filename)
            shutil.move(file_path, destination)
            moved = True
            break

    if not moved:
        destination = os.path.join(folder, "Others", filename)
        shutil.move(file_path, destination)

print("Files organized successfully!")