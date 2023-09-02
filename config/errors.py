import logging
import time
import telethon.errors
from settings import MY_ID

INITIAL_DELAY = 2
MAX_DELAY = 60
current_delay = INITIAL_DELAY

async def rate_limited_execute(task, client, user_id):
    """Увеличивает задержку при ошибке флуда, обрабатывает другие ошибки
    и информирует пользователя."""
    global current_delay
    while True:
        try:
            result = await task
            current_delay = INITIAL_DELAY
            return result

        except telethon.errors.FloodWaitError as e:
            error_message = 'Ошибка флуда. Ожидание {current_delay} секунд...'
            logging.warning(error_message)
            await client.send_message(MY_ID, error_message)
            time.sleep(current_delay)

            current_delay *= 2
            if current_delay > MAX_DELAY:
                current_delay = MAX_DELAY

        except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
            error_message = 'Ошибка регистрации.'
            logging.error(error_message)
            await client.send_message(MY_ID, error_message)
            return None

        except telethon.errors.rpcerrorlist.ChannelPrivateError as e:
            chat_name = e.chat_name if e.chat_name else 'Неизвестный канал/чат.'
            error_message = f"{chat_name} заблокировал бота."
            logging.error(error_message)
            await client.send_message(MY_ID, error_message)
            return None

        except Exception as e:
            error_message = f'Неожиданная ошибка: {e}'
            logging.error(error_message)
            await client.send_message(MY_ID, error_message)
            return None