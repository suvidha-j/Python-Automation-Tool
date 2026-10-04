# Python File Organizer Automation Tool

## Project Overview

This project is a Python automation tool that organizes files into separate folders based on their file extensions.

It is useful for automating repetitive file organization tasks.

## Features

- Automatically organizes files by type
- Supports images, documents, text files, audio and video files
- Creates category folders automatically
- Moves files into the correct folders
- Handles invalid folder paths
- Handles permission and operating system errors
- Skips files if they already exist in the destination

## File Categories

| Category | File Types |
|----------|------------|
| Images | JPG, JPEG, PNG, GIF |
| Documents | PDF, DOCX, DOC, XLSX, PPTX |
| Text | TXT, CSV |
| Audio | MP3, WAV |
| Videos | MP4, AVI, MKV |
| Others | Other file types |

## Technologies Used

- Python
- os module
- shutil module

## How It Works

1. The user provides the folder path.
2. The program reads the files in the folder.
3. It checks each file extension.
4. It identifies the appropriate category.
5. It creates the category folder if required.
6. It moves the file into the category folder.

## How to Run

Open the project folder in VS Code.

Run:

```bash
python file_organizer.py