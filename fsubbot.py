import Config
import logging
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from aiohttp import web
from ForceTG_Aerobot2.0 import web_server

PORT = "8080"

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Bot(Client):

    def __init__(aerobot):
        super().__init__(
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="ForceTG_Aerobot"),
        )

    async def start(aerobot):
         app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()        

# Run Bot
if __name__ == "__main__":
    try:
        await super().start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = aerobot.get_me().username
    print(f"@{uname} Bot Started Successfully By @AerodynamicV1Botz !")
    idle()
async def stop(aerobot, *args):
    super().stop()
    print("Bot stopped. Alvida!")

app = Bot()
app.run()
