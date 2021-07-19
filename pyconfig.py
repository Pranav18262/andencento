import os

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
HEROKU_API = os.getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
PY_SESSION = os.getenv("SESSION")
PREFIX = os.environ.get("PREFIX")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
MONGO_URI = os.getenv("MONGO_URI")
BOT_TOKEN = os.getenv("BOT_TOKEN")
