import discord
from discord.ext import commands

# Reading the token
with open("./secrets/bot-token.txt") as bot_token_file:
    token = bot_token_file.read()

# Initialize client
client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    """Checks if the bot is ready
    """
    print("Bot is ready 😁")


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print("{}: {}".format(author, content))


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, content)

client.run(token)
