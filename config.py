import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7984649091:AAETiBMARppfeGLpZ4tJMMvfTsBo53Ye78M")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "8012239"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "171e6f1bf66ed8dcc5140fbe827b6b08")

# Your Owner / Admin Id For Broadcast 7744665378
ADMINS = int(os.environ.get("ADMINS", "7744665378"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ftm:ftm@cluster0.8hbsnml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "ftm-src-pro")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
