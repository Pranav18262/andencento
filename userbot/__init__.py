import os
import sys
import time
op = os.environ.get("PYRO", None)
if {op} == "True" or "TRUE":
    os.system("pip install -r pyro.txt")
    from userbot.pyrogram import *
    app = client
else:
    exit
