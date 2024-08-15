import click
from prompt_operations import create_prompt, update_prompt, delete_prompt, archive_prompt
from lmm_interaction import send_prompt_to_llm

@click.group()
def cli():
    """Interactive Prompt Manager"""
    pass

@cli.command()
def prompt_management():
    click.echo("Prompt Management Menu:")
    click.echo("1. Add New Prompt")
    click.echo("2. Update Prompt")
    click.echo("3. Delete Prompt")
    click.echo("4. Archive Prompt")
    click.echo("5. Retire Prompt")
    choice = click.prompt("Choose an option", type=int)
    if choice == 1:
        prompt_name = click.prompt("Enter the prompt name")
        create_prompt(prompt_name)
    elif choice == 2:
        prompt_name = click.prompt("Enter the prompt name")
        update_prompt(prompt_name)
    elif choice == 3:
        prompt_name = click.prompt("Enter the prompt name")
        delete_prompt(prompt_name)
    elif choice == 4:
        prompt_name = click.prompt("Enter the prompt name")
        archive_prompt(prompt_name)
    elif choice == 5:
        prompt_name = click.prompt("Enter the prompt name")
        retire_prompt(prompt_name)
    else:
        click.echo("Invalid choice.")
