import os
import shutil


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx"],
    "Text": [".txt", ".csv"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"],
}


def get_category(file_extension):
    """Return the category for a file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def organize_files(folder_path):
    """Organize files in the selected folder."""
    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        print("Error: The given path is not a folder.")
        return

    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            continue

        _, extension = os.path.splitext(file_name)
        category = get_category(extension)

        category_folder = os.path.join(folder_path, category)

        try:
            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(category_folder, file_name)

            if os.path.exists(destination):
                print(f"Skipped: {file_name} already exists.")
                continue

            shutil.move(file_path, destination)
            print(f"Moved: {file_name} -> {category}/")

        except PermissionError:
            print(f"Permission denied: {file_name}")

        except OSError as error:
            print(f"Could not move {file_name}: {error}")


def main():
    print("===== PYTHON FILE ORGANIZER =====")

    folder_path = input("Enter folder path to organize: ").strip()

    if not folder_path:
        print("Folder path cannot be empty.")
        return

    organize_files(folder_path)

    print("\nFile organization completed!")


if __name__ == "__main__":
    main()