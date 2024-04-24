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


# Инициализация асинхронного клиента Socket.IO
sio = socketio.AsyncClient(reconnection=True, reconnection_delay=5)
api_url = 'https://api.telegram.org'

# Инициализация Telegram клиента (глобально)
telegram_client = TelegramClient(user_name, api_id, api_hash)

# Обработчик события подключения к WebSocket
@sio.event
async def connect():
    print('Бот запущен')
    await sio.emit('add-user', {'token': alert_token, "type": "alert_widget"})

# Обработчик события donation
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

# Функция для отправки сообщения в Telegram
async def send_telegram_message():
    await telegram_client.send_message('ifttt', 'Donate')

# Основная функция, запускающая всё приложение
async def main():
    await telegram_client.start()
    await sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')

    # Ожидание 59.5 минут перед остановкой программы
    await asyncio.sleep(3570)  # 59.5 минут * 60 секунд = 3570 секунд
    await sio.disconnect()
    await telegram_client.disconnect()

# Запуск приложения
if __name__ == "__main__":
    asyncio.run(main())
