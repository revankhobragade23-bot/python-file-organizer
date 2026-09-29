# Python File Organizer

A simple Python automation tool that organizes files into separate folders based on their file extensions.

## Features

- Organizes images
- Organizes PDFs
- Organizes documents
- Organizes videos
- Organizes audio files
- Organizes archive files
- Moves unknown file types to an `Others` folder
- Automatically creates required folders

## Folder Structure

Before:

```text
MyFolder/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
├── notes.txt
└── file.xyz

After running the program:

MyFolder/
├── Images/
│   └── photo.jpg
├── PDFs/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Documents/
│   └── notes.txt
├── Others/
│   └── file.xyz
└── Archives/

Technologies Used
Python
OS Module
Shutil Module
Requirements

Python 3.x

No external packages are required.

How to Run

Clone the repository:

git clone https://github.com/yourusername/python-file-organizer.git

Navigate to the project folder:

cd python-file-organizer

Run the program:

python file_organizer.py

Enter the path of the folder you want to organize.

Supported File Types
Images
.jpg
.jpeg
.png
.gif
.webp
Documents
.doc
.docx
.txt
.odt
PDFs
.pdf
Videos
.mp4
.mkv
.avi
.mov
Audio
.mp3
.wav
.aac
Archives
.zip
.rar
.7z
Concepts Practiced
File handling
Directory management
Loops
Dictionaries
Conditional statements
File extensions
Automation
Python built-in modules
Author

Revan Khobragade


### `.gitignore`

Is project ke liye practically kuch special ignore karna zaroori nahi hai, but repo me `.gitignore` rakhna hai toh:

```gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
Final repo:
python-file-organizer/
│
├── file_organizer.py
├── README.md
├── requirements.txt
└── .gitignore
