import os
import shutil

PROMPT_DIR = 'prompts'
ARCHIVE_DIR = 'archives'

def create_prompt(prompt_name):
    if not os.path.exists(PROMPT_DIR):
        os.makedirs(PROMPT_DIR)
    
    prompt_path = os.path.join(PROMPT_DIR, prompt_name)
    if os.path.exists(prompt_path):
        return f"Prompt file '{prompt_name}' already exists."
    else:
        with open(prompt_path, 'w') as f:
            f.write("Your prompt content here...")
        return f"Prompt file '{prompt_name}' created."

def update_prompt(prompt_name, new_content):
    prompt_path = os.path.join(PROMPT_DIR, prompt_name)
    if not os.path.exists(prompt_path):
        return f"Prompt file '{prompt_name}' does not exist."
    else:
        with open(prompt_path, 'w') as f:
            f.write(new_content)
        return f"Prompt file '{prompt_name}' updated."

def delete_prompt(prompt_name):
    prompt_path = os.path.join(PROMPT_DIR, prompt_name)
    if os.path.exists(prompt_path):
        os.remove(prompt_path)
        return f"Prompt file '{prompt_name}' deleted."
    else:
        return f"Prompt file '{prompt_name}' does not exist."

def archive_prompt(prompt_name):
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    
    prompt_path = os.path.join(PROMPT_DIR, prompt_name)
    archive_path = os.path.join(ARCHIVE_DIR, prompt_name)
    
    if os.path.exists(prompt_path):
        shutil.move(prompt_path, archive_path)
        return f"Prompt file '{prompt_name}' archived."
    else:
        return f"Prompt file '{prompt_name}' does not exist."
