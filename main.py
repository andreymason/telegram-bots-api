import os
import ast
import asyncio
from dotenv import load_dotenv
import json 
import re
import random
import string
from fastapi import FastAPI, Query
from telethon import events, functions
from telethon.sync import TelegramClient
from telethon.tl.types import Message

load_dotenv()

app = FastAPI()

class TelegramConnection:
    def __init__(self):
        self.client = None

    async def __aenter__(self):
        self.client = TelegramClient('name', os.environ["API_ID"], os.environ["API_HASH"])
        await self.client.start()
        return self.client

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.disconnect()

def message_to_json(message: Message) -> str:
    formatted_date = message.date.strftime("%m-%d-%Y %H:%M:%S")
    replies = []
    if message.reply_markup:
        replies = [button.text for row in message.reply_markup.rows for button in row.buttons]

    message_json = {
        "message": message.message,
        "date": formatted_date,
        "replies": replies
    }

    json_string = ast.literal_eval(f"{message_json}")
    
    return json_string

def generate_random_string(length=16):
    letters = string.ascii_letters  
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

@app.get("/authorize")
async def authorize():
    async with TelegramConnection() as client:

        title = 'Chat {}'.format(generate_random_string())

        groups = await client(functions.messages.CreateChatRequest(
            users=[91512510],
            title=title
        ))

        # select created chat
        chat = groups.chats[0]

        return {"group_id": chat.id}

@app.get("/")
async def send_message_and_get_response(text: str = None, button: int = None, group_id: int = None):
    async with TelegramConnection() as client:
        chat_id = group_id
        me = await client.get_me()
        sender_id = me.id

        if text is not None and button is None:
            await client.send_message(chat_id, text)

        await asyncio.sleep(1)

        async for message in client.iter_messages(chat_id):
            if message.sender_id != sender_id:
                if button is not None and text is None:
                    try:
                        await message.click(button)
                    except IndexError:
                        await message.click(-1)

                message_json = message_to_json(message)
                return message_json

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
