import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv'],
    "Audio": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Scripts": ['.py', '.js', '.html', '.css', '.cpp', '.java'],
    "Others": []
}

def get_file_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_directory(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            category = get_file_category(ext)

            category_folder = os.path.join(path, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            shutil.move(file_path, os.path.join(category_folder, file_name))

    print("Files organized successfully!")

if __name__ == "__main__":
    user_path = input("Enter the full path of the directory to organize: ").strip()
    organize_directory(user_path)
