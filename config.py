import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29732337"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "27c900a8bac51da6d0fd91aad09ef779")

#Database 
DB_URI = os.environ.get("DB_URI", "
mongodb+srv://eclipsecho:eclipsecho@eclipseecho.k3t9kne.mongodb.net/?retryWrites=true&w=majority&appName=EclipseEcho")
