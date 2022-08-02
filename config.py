
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "13820773"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "14dd075422f501a91407231fc98af817")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAjXCwapG2TqnvPp9gmxvSOh8aj7-nLUVu6edSIwVoNXZTlQTO1Kii-LHuW5RobLSyLH4tByVm2e7cLUHm8dWu_rMsn4H43lLBIG1yz1aWM-WPxFAuCtEUaHbAm0EK8N26RSkzzQlGHn95KPfFcWl0D4y9g77t49ZpgaRGpgoKE9d9O_L9TX8mNVZbq6Y1jT40dwF7Nw0u5BozDtGV2i1cyYRkGZLRhVf56ugAZlnVHwTMgn2WBwEjYaWzp8BvYtE7OP7ZGbqHWNtmiOmjJ7Yg5R2WCFcUonUDzLf9on7dyqSEH9lJhGRwoFTWOzO5EXtTaqPt-KYIWlMUUsACoCaJLAAAAAT4wwvYA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001751200479 -1001580194924")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
