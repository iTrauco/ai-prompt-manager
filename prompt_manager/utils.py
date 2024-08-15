import os

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
