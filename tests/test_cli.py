import click
from click.testing import CliRunner
from prompt_manager.cli import cli

def test_add_prompt():
    runner = CliRunner()
    result = runner.invoke(cli, ['add_prompt', 'test_prompt.txt'])
    assert result.exit_code == 0
    assert 'Adding prompt: test_prompt.txt' in result.output

def test_update_prompt():
    runner = CliRunner()
    result = runner.invoke(cli, ['update_prompt', 'test_prompt.txt', 'New content'])
    assert result.exit_code == 0
    assert 'Updating prompt: test_prompt.txt' in result.output

def test_delete_prompt():
    runner = CliRunner()
    result = runner.invoke(cli, ['delete_prompt', 'test_prompt.txt'])
    assert result.exit_code == 0
    assert 'Deleting prompt: test_prompt.txt' in result.output

def test_archive_prompt():
    runner = CliRunner()
    result = runner.invoke(cli, ['archive_prompt', 'test_prompt.txt'])
    assert result.exit_code == 0
    assert 'Archiving prompt: test_prompt.txt' in result.output

def test_send_prompt_to_llm():
    runner = CliRunner()
    result = runner.invoke(cli, ['send_prompt_to_llm', 'test_prompt.txt'])
    assert result.exit_code == 0
    assert 'Sending prompt: test_prompt.txt' in result.output
