import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "6273234785:AAGceR4arocROFq0YZAmZ0S4F729JG6Wu8c") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", "16217735")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "445a16e1f1554cc189673c6be5f5a72f") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "-1005570163408")) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://urluploader:urluploader@cluster0.uzzcbud.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
