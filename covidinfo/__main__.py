import asyncio
import importlib
import time

from covidinfo import setbot
from covidinfo.assistant import ALL_SETTINGS

BOT_RUNTIME = 0
HELP_COMMANDS = {}

loop = asyncio.get_event_loop()


async def get_runtime():
    return BOT_RUNTIME

async def reinitial():
    await setbot.start()
    await setbot.stop()

async def start_bot():
    print("----- Checking user and bot... -----")
    await reinitial()
    # sys.excepthook = except_hook
    # Assistant bot
    await setbot.start()
    for setting in ALL_SETTINGS:
        imported_module = importlib.import_module("covidinfo.assistant." + setting)
    # Nana userbot
    print("Assistant modules: " + str(ALL_SETTINGS))
    print("-----------------------")
    print("Bot run successfully!")
    await setbot.idle()


if __name__ == '__main__':
    BOT_RUNTIME = int(time.time())
    loop.run_until_complete(start_bot())
