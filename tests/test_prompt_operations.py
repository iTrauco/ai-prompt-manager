import os
from prompt_manager.prompt_operations import create_prompt, update_prompt, delete_prompt, archive_prompt

def test_create_prompt():
    result = create_prompt('test_prompt.txt')
    assert 'Prompt file \'test_prompt.txt\' created.' in result
    assert os.path.exists('prompts/test_prompt.txt')

def test_update_prompt():
    create_prompt('test_prompt.txt')
    result = update_prompt('test_prompt.txt', 'Updated content')
    assert 'Prompt file \'test_prompt.txt\' updated.' in result
    with open('prompts/test_prompt.txt', 'r') as file:
        content = file.read()
    assert content == 'Updated content'

def test_delete_prompt():
    create_prompt('test_prompt.txt')
    result = delete_prompt('test_prompt.txt')
    assert 'Prompt file \'test_prompt.txt\' deleted.' in result
    assert not os.path.exists('prompts/test_prompt.txt')

def test_archive_prompt():
    create_prompt('test_prompt.txt')
    result = archive_prompt('test_prompt.txt')
    assert 'Prompt file \'test_prompt.txt\' archived.' in result
    assert not os.path.exists('prompts/test_prompt.txt')
    assert os.path.exists('archives/test_prompt.txt')
