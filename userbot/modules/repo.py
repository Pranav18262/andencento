
from .. import app
from config import PREFIX
from pyrogram.types import Message
from pyrogram import filters
from .help import add_command_help
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

add_command_help(
          "repo", [
          ["`{PREFIX}repo`", "gives the repo link in inline button form"],
                        ],
)

@app.on_message (filters.command("repo", PREFIX) & filters.me)
async def repo(_, message: Message):
    texmt = f"[Repo🔥Stable](https://github.com/GODBOYX/PYROGOD) [Deploy🔥Stable](https://dashboard.heroku.com/new?template=https://github.com/GODBOYX/PyroPack)\n[Repo⚡Beta](https://github.com/GODBOYX/PyroGod-Beta) [Deploy⚡Beta](https://dashboard.heroku.com/new?template=https://github.com/GODBOYX/PyroPack-Beta)"
    await message.delete()
    await app.send_message(message.chat.id, texmt, disable_web_page_preview=True)
 
