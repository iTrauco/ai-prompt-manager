import click
import os
import requests

# Function to load prompts configuration
def load_prompts_config():
    config_path = os.path.expanduser("~/.prompts/config")
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(config_path, "r") as config_file:
        for line in config_file:
            if line.strip():
                key, value = line.strip().split("=", 1)
                if key == "PROMPTS_DIR":
                    return value
    raise ValueError("PROMPTS_DIR not found in the configuration file")

# Load configuration
PROMPTS_DIR = load_prompts_config()
ARCHIVE_DIR = os.path.join(PROMPTS_DIR, 'archives')

@click.group()
def cli():
    """Prompt Manager CLI"""
    pass

@cli.command()
@click.argument("prompt_name")
def add_prompt(prompt_name):
    """Add a new prompt file"""
    result = create_prompt(prompt_name)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
@click.argument("new_content")
def update_prompt(prompt_name, new_content):
    """Update an existing prompt file"""
    result = update_prompt(prompt_name, new_content)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
def delete_prompt(prompt_name):
    """Delete a prompt file"""
    result = delete_prompt(prompt_name)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
def archive_prompt(prompt_name):
    """Archive a prompt file"""
    result = archive_prompt(prompt_name)
    click.echo(result)

@cli.command()
@click.argument("prompt_name")
def send_prompt_to_llm(prompt_name):
    """Send a prompt to the LLM and get a response"""
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    if not os.path.exists(prompt_path):
        click.echo(f"Prompt file '{prompt_name}' does not exist.")
        return
    
    with open(prompt_path, 'r') as f:
        prompt_content = f.read()
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(LLM_API_URL, json={"prompt": prompt_content}, headers=headers)
    
    if response.status_code == 200:
        llm_response = response.json().get("response", "No response found.")
        click.echo(f"LLM Response: {llm_response}")
    else:
        click.echo(f"Failed to get response from LLM. Status code: {response.status_code}")

@cli.command()
def list_prompts():
    """List all prompt files"""
    if not os.path.isdir(PROMPTS_DIR):
        click.echo(f"Directory not found: {PROMPTS_DIR}")
        return
    prompts = [f for f in os.listdir(PROMPTS_DIR) if os.path.isfile(os.path.join(PROMPTS_DIR, f))]
    click.echo("\n".join(prompts))

# Add the implementation of the required functions
def create_prompt(prompt_name):
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    if os.path.exists(prompt_path):
        return f"Prompt file '{prompt_name}' already exists."
    with open(prompt_path, 'w') as f:
        f.write("")  # Create an empty file
    return f"Prompt file '{prompt_name}' created."

def update_prompt(prompt_name, new_content):
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    if not os.path.exists(prompt_path):
        return f"Prompt file '{prompt_name}' does not exist."
    with open(prompt_path, 'w') as f:
        f.write(new_content)
    return f"Prompt file '{prompt_name}' updated."

def delete_prompt(prompt_name):
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    if not os.path.exists(prompt_path):
        return f"Prompt file '{prompt_name}' does not exist."
    os.remove(prompt_path)
    return f"Prompt file '{prompt_name}' deleted."

def archive_prompt(prompt_name):
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    if not os.path.exists(prompt_path):
        return f"Prompt file '{prompt_name}' does not exist."
    archive_path = os.path.join(ARCHIVE_DIR, prompt_name)
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    os.rename(prompt_path, archive_path)
    return f"Prompt file '{prompt_name}' archived."

# Only run if this file is executed directly
if __name__ == "__main__":
    cli()
