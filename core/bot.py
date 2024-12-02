import os
import discord
import asyncio
from PIL import ImageGrab
from core.config import TOKEN
from core.os_info import create_directory, get_directory_path


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

        if message.content.lower().startswith('send'):
            directory_path = get_directory_path()

            create_directory(directory_path)

            screenshot = ImageGrab.grab()

            file_path = os.path.join(directory_path, "fullscreen_screenshot.png")

            screenshot.save(file_path)

            print(f"Full-screen screenshot saved as '{file_path}'")

            file = discord.File(file_path, filename="fullscreen_screenshot.png")

            await message.channel.send("Here is your photo!", file=file)

            os.remove(file_path)

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
