from telethon.sync import TelegramClient, events
from config.settings import ID, HASH
import logging

KEYWORDS = ['python']
STOPWORDS = ['senior']

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s, %(funcName)s, %(message)s, %(name)s'
)

client = TelegramClient('telejobot', ID, HASH)


async def get_channels_from_folder(folder_name):
    """Получение всех сообщений из заданной папки."""
    dialogs = await client.get_dialogs()
    return [dialog.entity for dialog in dialogs if dialog.is_channel]


async def monitor_channels(event):
    """Фильтрация и переадресация сообщений по заданным параметрам."""
    message = event.message.text.lower()
    if any(key in message for key in KEYWORDS) and not any(stop in message for stop in STOPWORDS):
        await event.message.forward_to('NickShinkov')


async def check_status(event):
    """Проверка работоспособности бота и получение списка отслеживаемых каналов."""
    channels = await get_channels_from_folder('Work')
    channel_names = [channel.title for channel in channels]
    response = "Статус бота: Запущен\nОтслеживаемые каналы:\n{}".format('\n'.join(channel_names))
    await event.respond(response)


async def setup_event_handlers():
    """Обработчик событий."""
    channels = await get_channels_from_folder('Work')
    client.add_event_handler(monitor_channels, events.NewMessage(chats=channels))
    client.add_event_handler(check_status, events.NewMessage(pattern='/status'))


if __name__ == '__main__':
    client.start()
    print('Бот запущен.')
    client.loop.run_until_complete(setup_event_handlers())
    client.run_until_disconnected()



