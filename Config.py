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
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgres://forcesubaerobot_user:cokOZ8DwqefWzkh3CM2IkkDmCiLtkxS3@dpg-ckb4lv1kms5s73c8gvv0-a.oregon-postgres.render.com/forcesubaerobot")
    BOT_USERNAME = os.environ.get('BOT_USERNAME', None)
    OWNER_ID=1484735126
    OWNER_ID=5708737143
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "AerodynamicV1_Update")
    if MUST_JOIN.startswith("@"):
        
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
    START_IMG= ""
    DATABASE_URL = ""
    BOT_USERNAME=""
    OWNER_ID=1484735126
    OWNER_ID=5708737143
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1484735126, 5708737143]
