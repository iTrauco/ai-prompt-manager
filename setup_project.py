
import os

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Project structure
project_name = "prompt-manager"
directories = [
    f"{project_name}/scripts",
    f"{project_name}/setup"
]
files = {
    f"{project_name}/.gitignore": '''
# Ignore development and system files
*.pyc
__pycache__/
*.pyo
*.pyd
*.swp
*.bak
*.tmp
*.log
*.DS_Store
.vscode/
.idea/
.env
.venv/
node_modules/
dist/
build/
.coverage
*.egg-info/
.cache/
''',
    f"{project_name}/README.md": '''
# Prompt Manager

## Overview

The Prompt Manager is a comprehensive utility for managing prompt files and directories. It supports both project-specific and system-wide prompt management workflows.

## Features

- List, add, and delete prompt files.
- Detect recent prompt files in the Downloads folder.
- Move and delete selected or all detected prompt files.
- Automatically update .gitignore files with prompt exclusion logic.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/prompt-manager.git
cd prompt-manager
```

### Setup

Run the setup script to install the prompt manager:

```bash
bash setup/install.sh
```

## Usage

Run the prompt manager script:

```bash
bash scripts/prompt_manager.sh
```

## Project Structure

```
prompt-manager/
|
├── .gitignore
├── README.md
├── scripts/
|   └── prompt_manager.sh
└── setup/
    └── install.sh
```
''',
    f"{project_name}/scripts/prompt_manager.sh": '''
#!/bin/bash

PROMPT_DIR="./prompts"
DOWNLOADS_DIR="$HOME/Downloads"

# Ensure the prompt directory exists
mkdir -p $PROMPT_DIR

# Function to list all prompt files
list_prompts() {
    echo -e "\n📂 Current prompt files in $PROMPT_DIR:"
    ls $PROMPT_DIR | grep -i prompt
}

# Function to add a new prompt file
add_prompt() {
    read -p "Enter the name of the new prompt file (including 'prompt' in the name): " prompt_name
    if [[ "$prompt_name" != *prompt* ]]; then
        echo "❌ The file name must include the word 'prompt'."
        return
    fi
    touch "$PROMPT_DIR/$prompt_name"
    echo "✅ Created $PROMPT_DIR/$prompt_name."
}

# Function to delete a prompt file
delete_prompt() {
    read -p "Enter the name of the prompt file to delete: " prompt_name
    if [ -f "$PROMPT_DIR/$prompt_name" ]; then
        rm "$PROMPT_DIR/$prompt_name"
        echo "✅ Deleted $PROMPT_DIR/$prompt_name."
    else
        echo "❌ File not found: $PROMPT_DIR/$prompt_name."
    fi
}

# Function to list recent prompt files in Downloads
list_downloaded_prompts() {
    echo -e "\n📥 Recent prompt files in $DOWNLOADS_DIR:"
    find $DOWNLOADS_DIR -maxdepth 1 -type f -iname "*prompt*" -mtime -7
}

# Function to move selected prompt files from Downloads to prompts directory
move_prompts() {
    list_downloaded_prompts
    echo -e "\nEnter the names of the files to move (separate with spaces) or type 'all' to move all:"
    read -a prompt_files

    if [[ "${prompt_files[0]}" == "all" ]]; then
        find $DOWNLOADS_DIR -maxdepth 1 -type f -iname "*prompt*" -mtime -7 -exec mv {} $PROMPT_DIR \;
        find $DOWNLOADS_DIR -maxdepth 1 -type f -iname "*prompt*" -mtime -7 -exec rm {} \;
        echo "✅ All prompt files moved and deleted from $DOWNLOADS_DIR."
    else
        for file in "${prompt_files[@]}"; do
            if [ -f "$DOWNLOADS_DIR/$file" ]; then
                mv "$DOWNLOADS_DIR/$file" "$PROMPT_DIR"
                rm "$DOWNLOADS_DIR/$file"
                echo "✅ Moved and deleted $file."
            else
                echo "❌ File not found: $file."
            fi
        done
    fi
}

# Function to update .gitignore files
update_gitignore() {
    if [ -f .gitignore ]; then
        if ! grep -q '*prompt*' .gitignore; then
            echo -e "\n# Ignore all files and directories containing 'prompt' in their names, including dotfiles\n*prompt*\n.prompt*\nprompt/\nprompts/" >> .gitignore
            echo "✅ Updated project .gitignore."
        fi
    fi

    if [ -f ~/.gitignore_global ]; then
        if ! grep -q '*prompt*' ~/.gitignore_global; then
            echo -e "\n# Ignore all files and directories containing 'prompt' in their names, including dotfiles\n*prompt*\n.prompt*\nprompt/\nprompts/" >> ~/.gitignore_global
            echo "✅ Updated global .gitignore."
        fi
    fi
}

while true; do
    echo -e "\n🎉 Welcome to the Project Prompt Manager! 🎉"
    echo "1. List all prompt files"
    echo "2. Add a new prompt file"
    echo "3. Delete a prompt file"
    echo "4. List recent prompt files in Downloads"
    echo "5. Move selected or all prompt files from Downloads to prompts directory"
    echo "6. Update .gitignore files"
    echo "7. Exit"
    read -p "Select an option [1-7]: " option

    case $option in
        1)
            list_prompts
            ;;
        2)
            add_prompt
            ;;
        3)
            delete_prompt
            ;;
        4)
            list_downloaded_prompts
            ;;
        5)
            move_prompts
            ;;
        6)
            update_gitignore
            ;;
        7)
            echo "👋 Exiting the Project Prompt Manager. Goodbye!"
            exit 0
            ;;
        *)
            echo "❌ Invalid option. Please select a number between 1 and 7."
            ;;
    esac
done
''',
    f"{project_name}/setup/install.sh": '''
#!/bin/bash

echo "Installing Prompt Manager..."

# Ensure scripts are executable
chmod +x scripts/prompt_manager.sh

# Update global .gitignore
if [ ! -f ~/.gitignore_global ]; then
    touch ~/.gitignore_global
fi

if ! grep -q '*prompt*' ~/.gitignore_global; then
    echo -e "\n# Ignore all files and directories containing 'prompt' in their names, including dotfiles\n*prompt*\n.prompt*\nprompt/\nprompts/" >> ~/.gitignore_global
    git config --global core.excludesfile ~/.gitignore_global
    echo "✅ Updated global .gitignore."
fi

echo "Prompt Manager installation complete."
'''
}

# Create directories
for directory in directories:
    create_directory(directory)

# Create files
for path, content in files.items():
    create_file(path, content)

print(f"Project '{project_name}' setup complete.")
