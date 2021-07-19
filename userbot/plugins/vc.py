from userbot import *

@bot.on(admin_cmd(pattern="playvc$",
))
async def _(e):
    zz = await eor(e, "`VC bot started...`")
    er, out = await bash("python vcbot/bot.py")
    LOGS.info(er)
    LOGS.info(out)
    if er:
        msg = f"Failed {er}\n\n{out}"
        if len(msg) > 4096:
            with open("vc-error.txt", "w") as f:
                f.write(msg.replace("`", ""))
            await e.reply(file="vc-error.txt")
            await zz.delete()
            remove("vc-error.txt")
            return
        await zz.edit(msg)
