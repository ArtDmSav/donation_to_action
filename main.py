import socketio
import aiohttp
import json
import asyncio
from telethon import TelegramClient


api_id = 304993932
api_hash = 'jnsnksjnv8wf4r3e8gbere98383k'
user_name = '1111111111'
tg_user_id = 1111111111
alert_token = 'jnsvnskkjnsdsf'
tg_bot_token = '718385733:AAsjnvssv-dfijvnnosfnvsfn'


# Initializing an asynchronous client Socket.IO
sio = socketio.AsyncClient(reconnection=True, reconnection_delay=5)
api_url = 'https://api.telegram.org'

# Initializing the Telegram client (глобально)
telegram_client = TelegramClient(user_name, api_id, api_hash)

# Обработчик события подключения к WebSocket
@sio.event
async def connect():
    print('Бот запущен')
    await sio.emit('add-user', {'token': alert_token, "type": "alert_widget"})

# Event handler donation
@sio.event
async def donation(data):
    event = json.loads(data)
    print(event)
    async with aiohttp.ClientSession() as session:
        payload = {
            'chat_id': tg_user_id,
            'text': f'New donate:\n{event["username"]} - {event["amount"]} {event["currency"]}\n{event["message"]}'
        }
        await session.get(f'{api_url}/bot{tg_bot_token}/sendMessage', params=payload)
    await send_telegram_message()

# Function for sending a message in Telegram
async def send_telegram_message():
    await telegram_client.send_message('ifttt', 'Donate')

# The main function that runs the entire application
async def main():
    await telegram_client.start()
    await sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')

    # Necessary for my task (optional). Waiting 59.5 minutes before stopping the program
    await asyncio.sleep(3570)  # 59.5 minutes * 60 seconds = 3570 seconds
    await sio.disconnect()
    await telegram_client.disconnect()

# Launch the application
if __name__ == "__main__":
    asyncio.run(main())
