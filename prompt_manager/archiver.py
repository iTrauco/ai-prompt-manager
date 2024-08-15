import shutil
import os

ARCHIVE_DIR = 'archives'

def archive_prompt(prompt_name):
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    
    prompt_path = os.path.join('prompts', prompt_name)
    archive_path = os.path.join(ARCHIVE_DIR, prompt_name)
    
    if os.path.exists(prompt_path):
        shutil.move(prompt_path, archive_path)
        return f"Prompt file '{prompt_name}' archived."
    else:
        return f"Prompt file '{prompt_name}' does not exist."
