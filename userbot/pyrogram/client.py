import logging
import sys
import time
import motor.motor_asyncio
import pyromod.listen
from pyrogram import Client, errors
from pyconfig import API_HASH, API_ID, PY_SESSION, BOT_TOKEN
import logging



StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH
PY_SESSION = PY_SESSION
BOT_TOKEN = BOT_TOKEN


iamnoob = Client(PY_SESSION, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    
