import os

def organize_files(directory="."):
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            file_ext = os.path.splitext(filename)[1]
            if not os.path.exists(file_ext):
                os.makedirs(file_ext)
            os.rename(filename, os.path.join(file_ext, filename))

directory = input("Enter directory path (default is current directory): ")
organize_files(directory or ".")
