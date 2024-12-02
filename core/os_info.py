import os
import platform

def get_directory_path():
    if platform.system() == "Windows":
        return r"C:\ProgramImportance"

    elif platform.system() == "Darwin":
        return os.path.expanduser("~/ProgramImportance")

    elif platform.system() == "Linux":
        return os.path.expanduser("~/ProgramImportance")

    else:
        raise EnvironmentError("Unsupported operating system")

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created successfully.")
        except PermissionError:
            print(f"Permission denied. You need elevated permissions to create directories in this location.")
            exit()
