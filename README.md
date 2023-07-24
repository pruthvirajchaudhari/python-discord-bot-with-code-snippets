# Python Discord Bot with Code Snippets and Debugging Assistance

This repository contains a Python Discord bot that allows users to access code snippets and get basic debugging assistance for Python code. The bot uses the Discord API and the OpenAI API for providing code suggestions.

## Prerequisites

Before running the bot, you need to have the following:

1. **Discord Bot Token**: Obtain a bot token from the [Discord Developer Portal](https://discord.com/developers/applications). Replace `'YOUR_BOT_TOKEN'` with the actual bot token in the script.

2. **OpenAI API Key**: Obtain an API key from [OpenAI](https://openai.com/). Replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key in the script.

3. **Python 3.x**: Make sure you have Python 3.x installed on your system.

## Installation

1. Clone this repository to your local machine.

2. Install the required Python packages by running the following command:

```bash
pip install discord.py openai
```

## Configuration

Replace the placeholder values in the script with your actual Discord bot token and OpenAI API key.

```python
token = 'YOUR_BOT_TOKEN'
openai.api_key = 'YOUR_OPENAI_API_KEY'
```

## Usage

1. Run the bot using Python:

```bash
python bot.py
```

2. Once the bot is online, it will be ready to respond to commands in your Discord server.

## Bot Commands

The bot supports the following commands:

### 1. !show_help

Displays a help message containing all available bot commands.

### 2. !snippet <snippet_name>

Retrieves a code snippet for a specific task. Replace `<snippet_name>` with the desired code snippet's name.

Example: `!snippet hello`

### 3. !debug <your_code>

Provides basic debugging assistance for your Python code. Replace `<your_code>` with the Python code you want to debug.

Example: `!debug print("Hello, world!")`

## Customization

You can customize the code snippets available in the bot by modifying the `code_snippets` dictionary in the script. Add or remove code snippets as needed.

```python
code_snippets = {
    'hello': 'print("Hello, world!")',
    'add': 'result = 2 + 2',
    # Add more code snippets here...
}
```

Additionally, you can adjust the bot's behavior and settings by modifying the script according to your requirements.

## Note

The debugging assistance provided by the bot is limited to basic Python code evaluation. For more complex scenarios, consider extending the functionality or using specialized tools.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the developers of [discord.py](https://discordpy.readthedocs.io/en/stable/) and [OpenAI API](https://platform.openai.com/), which made building this bot possible.

Feel free to contribute to the project or suggest improvements by creating a pull request or opening an issue. Enjoy using the Python Discord Bot with Code Snippets and Debugging Assistance!
