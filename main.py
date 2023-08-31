from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from config.settings import ID, HASH

client = TelegramClient('anon', ID, HASH)

