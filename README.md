# Terminal Prompt Manager

## 🚧 Under Development 🚧

The Terminal Prompt Manager is an innovative CLI interactive shell program designed to revolutionize how developers interact with Large Language Models (LLMs) directly from the terminal. By leveraging the power and precision of Unix utilities, this tool aims to streamline prompt development, management, training, and interaction processes, offering a level of customization and efficiency that surpasses traditional AI tools in IDEs.

## 📌 Current Status

The baseline workflows for the Terminal Prompt Manager have been established and are functional. We are now focusing on introducing more advanced features, particularly around managing and setting specific LLMs by version and model number, starting with integration for the chatgpt-cli.

## 🎯 Long-Term Vision

Our ultimate goal is to empower developers with a system-level tool that allows for the creation of highly customized, rapid workflows. By integrating deeply with the operating system and utilizing the full power of command-line utilities, the Terminal Prompt Manager offers a degree of precision and customizability that GUI-based AI tools simply cannot match.

## 🌟 Key Features

- **Interactive Shell**: Develop and manage prompts for LLMs directly from your terminal.
- **Unix Utility Integration**: Harness the power of `awk`, `sed`, `grep`, pipes, and more to process input/output with unparalleled precision.
- **LLM Interaction**: Send prompts to LLMs and receive responses without leaving your terminal environment.
- **Prompt Management**: Easily create, update, delete, and organize your prompts.
- **Clipboard Integration**: Instantly copy LLM outputs or generated commands to your system clipboard for immediate use.
- **Bulk Editing**: Leverage sed and line-specific targeting for efficient bulk edits of entire files based on LLM suggestions.
- **System-Level Customization**: Create aliases and custom scripts for lightning-fast access to your most-used prompts and workflows.
- **Workflow Automation**: Chain commands and prompts to create sophisticated, automated processes tailored to your specific development needs.

## 🚀 Why Choose Terminal Prompt Manager?

- **Unmatched Precision**: Leverage the full power of Unix utilities for text processing and manipulation that GUI tools can't match.
- **Infinite Customizability**: Create custom aliases, functions, and scripts to tailor the tool to your exact needs.
- **Speed and Efficiency**: Execute complex operations with a few keystrokes, faster than any point-and-click interface.
- **Seamless Integration**: Works with your existing terminal-based workflows and tools.
- **Cross-Platform**: Works on any system with a Unix-like terminal, ensuring consistency across different development environments.

## 🛠 How It Works

1. **Develop Prompts**: Create and refine prompts directly in the terminal.
2. **Process Input**: Use Unix utilities to prepare your input:
   ```bash
   sed -n '10,20p' file.py | your-cli-command send-to-llm "refactor_code"
   ```
3. **Interact with LLMs**: Send processed input to LLMs and receive responses.
4. **Apply Changes**: Use the output to make precise changes:
   ```bash
   your-cli-command get-last-response | sed -i -f - file.py
   ```
5. **Automate Workflows**: Create aliases for your most common operations:
   ```bash
   alias quick-refactor='your-cli-command send-to-llm "refactor_prompt" | sed -f - target_file.py'
   ```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Access to an LLM API (e.g., OpenAI GPT-3)

### Installation

```bash
git clone https://github.com/yourusername/terminal-prompt-manager.git
cd terminal-prompt-manager
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
LLM_API_KEY=your_api_key_here
LLM_API_ENDPOINT=https://api.example.com/v1
```

### Basic Usage

```bash
python cli.py develop-prompt "My new prompt"
python cli.py send-to-llm "prompt_name" < input.txt
python cli.py apply-changes "prompt_name" file.txt
```

## 📘 Advanced Usage Example: Targeted Code Refactoring

Let's walk through a real-world example of how the Terminal Prompt Manager can help you quickly refactor a specific part of your code:

1. **Select the target code**: Use `sed` to extract lines 15-30 from your Python file:

   ```bash
   sed -n '15,30p' my_file.py > target_code.txt
   ```

2. **Send to LLM for refactoring**:

   ```bash
   cat target_code.txt | your-cli-command send-to-llm "refactor_for_performance" > llm_suggestions.sed
   ```

3. **Review and apply changes**:

   ```bash
   # Review suggestions
   cat llm_suggestions.sed

   # Apply changes and copy to clipboard
   sed -i '15,30{
     r llm_suggestions.sed
     d
   }' my_file.py | xclip -selection clipboard
   ```

4. **Create an alias for this workflow**:

   ```bash
   echo 'alias quick-refactor="sed -n \"\$1,\$2p\" \$3 | your-cli-command send-to-llm \"refactor_for_performance\" | sed -i \"\$1,\$2{r /dev/stdin\nd}\" \$3 | xclip -selection clipboard"' >> ~/.bashrc
   ```

   Now you can use:

   ```bash
   quick-refactor 15 30 my_file.py
   ```

This workflow allows you to:
- Target specific line numbers in your source file
- Get LLM suggestions for refactoring
- Automatically apply changes to the original file
- Copy the changes to your clipboard for easy reviewing or further editing

By leveraging Unix utilities like `sed` and `xclip`, along with the power of LLMs, you can perform complex code modifications with just a few commands. This level of precision and efficiency is hard to achieve with traditional IDE-based AI tools.

## 🔄 Comparison: ChatGPT CLI vs Terminal Prompt Manager

### Typical ChatGPT CLI Interaction:

```bash
# ChatGPT CLI
chatgpt "Refactor this Python function to improve performance:
def slow_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i * 2)
    return result"
```

This interaction:
- Requires manual copying of code into the prompt
- Provides a single, static response
- Leaves implementation of suggestions to the user

### Terminal Prompt Manager Potential:

```bash
# Terminal Prompt Manager
cat my_script.py | awk '/def slow_function/,/^$/' | \
your-cli-command send-to-llm "refactor_for_performance" | \
sed -i '/def slow_function/,/^$/c\' my_script.py
```

This interaction:
- Automatically extracts the relevant function from the file
- Sends it to the LLM for refactoring
- Applies the changes directly to the original file
- Can be easily customized and extended with Unix utilities

## 🔮 Future Plans

In the coming updates, we plan to introduce:

1. **LLM Version Management**: Ability to specify and switch between different LLM versions and models.
   ```bash
   your-cli-command set-llm gpt-4
   your-cli-command set-llm chatgpt-3.5-turbo
   ```

2. **Model-Specific Prompts**: Develop and manage prompts tailored to specific LLM versions.
   ```bash
   your-cli-command develop-prompt --model gpt-4 "Advanced code refactoring"
   ```

3. **Comparative Analysis**: Run the same prompt across multiple LLM versions and compare outputs.
   ```bash
   your-cli-command compare-llms "Optimize this algorithm" gpt-3.5-turbo gpt-4
   ```

4. **Integration with Popular LLM CLIs**: Seamless interaction with tools like chatgpt-cli, allowing users to leverage existing ecosystems.

These features will provide unprecedented control and flexibility in LLM interactions, setting the Terminal Prompt Manager apart as a powerful tool for developers and researchers alike.

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests, report issues, or request features.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- The Unix philosophy and its powerful text processing tools
- The open-source community for inspiration and support

---

**Note**: This project is still under active development. Features and commands may change. We appreciate your patience and feedback as we work towards a stable release!
