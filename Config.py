import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 16574790))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "c408c6b40e1ebd04b76c7d04a8de1dad")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5658314356:AAEIWcIyXBsQhRrltN_Nki6Ra5GcrTY522s")
    START_IMG = os.environ.get('START_IMG', None)
    BOT_USERNAME = os.environ.get('BOT_USERNAME', None)
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
