import os
PYRO = os.environ.get("PYRO", None)
if {PYRO} == "True":
    from pyrogram import idle, Client, filters
    from userbot import app, LOGGER
    from userbot.modules import *
    import os
    print("Andencento Started \nPowered By pyrogram && Andencento\n(C) ANDENCENTO USERBOT")
    app.run()
except BaseException:
    pass

import glob
import os
import sys
from pathlib import Path
from sys import argv

import telethon.utils
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from config import Config
from . import *
from .utils import *
from .session.main import *

    
# let's get the bot ready                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    Andencento.me = await bot.get_me() 
    Andencento.uid = telethon.utils.get_peer_id(bot.me)

if len(argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.tgbot = None
    if Config.BOT_TOKEN is not None:
        print("CHECKING BOT USERNAME")
        # ForTheGreatrerGood of beautification
        Andencento.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        Andencento.loop.run_until_complete(add_bot(Var.BOT_TOKEN))
        print("CHECKING SUCESS")
    else:
        Andencento.start()

async def mod():
    await asst()
    await plugs()
    await addons()

Andencento.loop.run_until_complete(mod())
Andencento.loop.create_task(op())
Andencento.loop.create_task(Andencentoiosop())
print("Andencento Deployed And Working Fine")

if len(sys.argv) not in (1, 3, 4):
    Andencento.disconnect()
else:
    Andencento.run_until_disconnected()
    noob.run_until_disconnected()
