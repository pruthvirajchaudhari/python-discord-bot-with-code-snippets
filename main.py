import discord
from discord.ext import commands
import openai

# Replace 'YOUR_BOT_TOKEN' with the actual bot token you obtained from the Discord Developer Portal
token ='MTEzMjI5MjI4NjgxMDY4OTU1Ng.Glw82D.lbjv7nIQxdKpGwkONbqVZ1tn76QJCj8eV0cVAA'

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

# Create an instance of Intents with the 'privileged_messages' intent enabled
intents = discord.Intents.default()
intents.typing = False  # You can enable or disable specific intents as per your needs
intents.message_content = True  # Enable the privileged message content intent

# Create a bot instance with the Intents and a command prefix (e.g., '!')
bot = commands.Bot(command_prefix='!', intents=intents)

# Code snippets dictionary - Replace these with your own code snippets
code_snippets = {
    'hello': 'print("Hello, world!")',
    'add': 'result = 2 + 2',
    # Add more code snippets here...
}

# Custom help command
@bot.command()
async def show_help(ctx):
    help_message = """
    **Python Bot Help**
    Use the following commands:
    !show_help - Show this help message.
    !snippet <snippet_name> - Get a code snippet for a specific task (e.g., !snippet hello).
    !debug <your_code> - Get basic debugging assistance for your Python code.
    """
    await ctx.send(help_message)

# Code snippet command
@bot.command()
async def snippet(ctx, snippet_name):
    snippet = code_snippets.get(snippet_name.lower())
    if snippet:
        await ctx.send(f'{ctx.author.mention} Here is the code snippet for {snippet_name}:\n```python\n{snippet}\n```')
    else:
        await ctx.send(f'{ctx.author.mention} Snippet "{snippet_name}" not found.')

# Debug command
@bot.command()
async def debug(ctx, *, code):
    try:
        # Attempt to evaluate the provided code
        result = eval(code)
        await ctx.send(f'{ctx.author.mention} Result: `{result}`')
    except Exception as e:
        # Send the code to ChatGPT for assistance
        try:
            chatgpt_response = openai.Completion.create(
                engine="text-davinci-002",  # You may choose a different engine if needed
                prompt=code,
                max_tokens=150,  # Adjust the max tokens as per your needs
            )
            suggestion = chatgpt_response.choices[0].text.strip()
            await ctx.send(f'{ctx.author.mention} Error: `{type(e).__name__} - {e}`\nSuggestion: `{suggestion}`')
        except Exception as chatgpt_error:
            await ctx.send(f'{ctx.author.mention} Error getting assistance from ChatGPT: {type(chatgpt_error).__name__} - {chatgpt_error}')

# Run the bot
bot.run(token)
