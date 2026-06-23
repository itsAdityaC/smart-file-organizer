# Smart File Organizer 

A simple Python automation project that automatically organizes files in a folder into categorized directories based on their file types.

---

##  Features

- Automatically scans a given folder
- Creates required folders if they don’t exist
- Sorts files into:
  - Images
  - Documents
  - Videos
  - Others
- Moves files based on file extensions
- Uses Python `os` and `shutil` modules

---

## Technologies Used

- Python 3
- os module
- shutil module

---

##  Project Structure
smart-file-organizer/
│
├── file_organizer.py
└── README.md


---

##  How to Run

1. Clone the repository
git clone: https://github.com/ItsAdityaC/smart-file-organizer.git
2. Open the project folder
3. Run the Python file:

```bash
python file_organizer.py

Enter the folder path you want to organize
Example
Downloads/
├── photo.jpg
├── resume.pdf
├── movie.mp4
├── notes.txt

After running
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Videos/
│   └── movie.mp4
├── Others/
│   └── notes.txt

Author

Aditya Chaurasia
