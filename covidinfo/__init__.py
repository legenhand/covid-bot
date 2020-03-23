from pyrogram import Client

from covidinfo.config import Config

ASSISTANT_BOT_TOKEN = Config.ASSISTANT_BOT_TOKEN
BOT_SESSION = Config.ASSISTANT_SESSION
api_id = Config.api_id
api_hash = Config.api_hash
ASSISTANT_WORKER = Config.ASSISTANT_WORKER

setbot = Client(BOT_SESSION, api_id=api_id, api_hash=api_hash, bot_token=ASSISTANT_BOT_TOKEN, workers=ASSISTANT_WORKER)
