from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import START_IMG

# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
@Client.on_message(filters.text & filters.incoming & filters.command("help@Aero_Force2_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("help@Aero_Force_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    await msg.reply_photo(
        START_IMG,
        caption="**ʜᴇʀᴇ's ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ?**\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
