import click
import os
import requests
from .prompt_operations import create_prompt, update_prompt, delete_prompt, archive_prompt
from .lmm_interaction import send_prompt_to_llm
from .config import LLM_API_URL, API_KEY


PROMPT_DIR = 'prompts'
ARCHIVE_DIR = 'archives'

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
    prompt_path = os.path.join(PROMPT_DIR, prompt_name)
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

if __name__ == '__main__':
    cli()
