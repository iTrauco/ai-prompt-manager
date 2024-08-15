import os
from prompt_manager.utils import ensure_directory_exists, read_file, write_file

def test_ensure_directory_exists():
    test_dir = 'test_dir'
    ensure_directory_exists(test_dir)
    assert os.path.exists(test_dir)
    os.rmdir(test_dir)  # Clean up

def test_read_write_file():
    test_file = 'test_file.txt'
    write_file(test_file, 'Test content')
    content = read_file(test_file)
    assert content == 'Test content'
    os.remove(test_file)  # Clean up
