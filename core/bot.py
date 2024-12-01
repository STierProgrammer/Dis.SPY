import discord
import asyncio
from core.config import TOKEN

async def start_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.lower().startswith('hello'):
            await message.channel.send('Hello!')

    await client.start(TOKEN)

def run_bot():
    try:
        asyncio.run(start_bot())

    except KeyboardInterrupt:
        print("Bot stopped manually.")

    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_bot()
