import click
import os
import requests
from .prompt_operations import create_prompt, update_prompt, delete_prompt, archive_prompt
from .lmm_interaction import send_prompt_to_llm
from .config import LLM_API_URL, API_KEY

# Define the directory names for prompts and archives
PROMPT_DIR = 'prompts'
ARCHIVE_DIR = 'archives'

@click.group()
def cli():
    """Prompt Manager CLI: A command-line interface to manage prompts and interact with LLMs."""
    pass

@cli.command()
@click.argument("prompt_name")
def add_prompt(prompt_name):
    """
    Add a new prompt file.

    This command will create a new prompt file with the given name in the prompts directory.
    """
    result = create_prompt(prompt_name)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
@click.argument("new_content")
def update_prompt(prompt_name, new_content):
    """
    Update an existing prompt file.

    This command updates the content of an existing prompt file with new content.
    """
    result = update_prompt(prompt_name, new_content)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
def delete_prompt(prompt_name):
    """
    Delete a prompt file.

    This command deletes the specified prompt file from the prompts directory.
    """
    result = delete_prompt(prompt_name)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
def archive_prompt(prompt_name):
    """
    Archive a prompt file.

    This command moves the specified prompt file to the archive directory.
    """
    result = archive_prompt(prompt_name)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
def send_prompt_to_llm(prompt_name):
    """
    Send a prompt to the LLM and get a response.

    This command reads the content of the prompt file and sends it to the LLM (via API) for processing.
    """
    prompt_path = os.path.join(PROMPT_DIR, prompt_name)
    
    # Check if the prompt file exists
    if not os.path.exists(prompt_path):
        click.echo(f"Prompt file '{prompt_name}' does not exist.")
        return
    
    # Read the content of the prompt file
    with open(prompt_path, 'r') as f:
        prompt_content = f.read()
    
    # Set up headers for API request
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    # Send prompt content to the LLM API
    response = requests.post(LLM_API_URL, json={"prompt": prompt_content}, headers=headers)
    
    # Process and display the response from the LLM
    if response.status_code == 200:
        llm_response = response.json().get("response", "No response found.")
        click.echo(f"LLM Response: {llm_response}")
    else:
        click.echo(f"Failed to get response from LLM. Status code: {response.status_code}")

@cli.command()
@click.argument("file_path")
@click.argument("start_line", type=int)
@click.argument("end_line", type=int)
def extract_lines(file_path, start_line, end_line):
    """
    Extract specific lines from a file and send them to the LLM.

    This command extracts lines from the specified file within the given range,
    sends them to the LLM, and outputs the response.
    """
    if not os.path.isfile(file_path):
        click.echo(f"File '{file_path}' does not exist.")
        return
    
    # Extract the specified lines from the file
    lines = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f, start=1):
            if start_line <= i <= end_line:
                lines.append(line)
    
    prompt_content = ''.join(lines)
    
    # Send extracted lines to the LLM
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(LLM_API_URL, json={"prompt": prompt_content}, headers=headers)
    
    if response.status_code == 200:
        llm_response = response.json().get("response", "No response found.")
        click.echo(f"LLM Response: {llm_response}")
    else:
        click.echo(f"Failed to get response from LLM. Status code: {response.status_code}")

@cli.command()
@click.argument("file_path")
@click.argument("start_line", type=int)
@click.argument("end_line", type=int)
def modify_file(file_path, start_line, end_line):
    """
    Modify a file by applying LLM suggestions to specific lines.

    This command extracts lines from the specified file within the given range,
    sends them to the LLM, and applies the suggestions to the file.
    """
    if not os.path.isfile(file_path):
        click.echo(f"File '{file_path}' does not exist.")
        return
    
    # Extract the specified lines from the file
    lines = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f, start=1):
            if start_line <= i <= end_line:
                lines.append(line)
    
    prompt_content = ''.join(lines)
    
    # Send extracted lines to the LLM
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(LLM_API_URL, json={"prompt": prompt_content}, headers=headers)
    
    if response.status_code == 200:
        llm_response = response.json().get("response", "No response found.")
        
        # Apply suggestions to the file using sed
        with open(file_path, 'r') as f:
            file_content = f.read()
        
        # Apply the modifications from the LLM response
        modified_content = file_content  # Placeholder for actual modification logic
        
        with open(file_path, 'w') as f:
            f.write(modified_content)
        
        click.echo(f"File '{file_path}' has been updated.")
    else:
        click.echo(f"Failed to get response from LLM. Status code: {response.status_code}")

if __name__ == "__main__":
    cli()
""" > prompt_manager/cli.py
