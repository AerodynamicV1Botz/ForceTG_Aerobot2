import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 16574790))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "c408c6b40e1ebd04b76c7d04a8de1dad")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5219214161:AAFudzJ_ixUrexsdEUPFNWxynDahgm7P96g")
    START_IMG = os.environ.get('START_IMG', "https://te.legra.ph/file/023e6daf966ba99871b80.jpg")
    BOT_USERNAME = os.environ.get('BOT_USERNAME', "@Aero_Force_Subscriber_Bot")
    OWNER_ID=1484735126
    OWNER_ID=5708737143
    MUST_JOIN = os.environ.get('MUST_JOIN', )
    if MUST_JOIN.startswith("@"):
        
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
    START_IMG= ""
    BOT_USERNAME=""
    OWNER_ID=1484735126
    OWNER_ID=5708737143
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1484735126, 5708737143]
