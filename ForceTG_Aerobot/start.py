from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from Config import START_IMG

# Start Message
@Client.on_message(filters.private & filters.text & filters.incoming & filters.command("start"))
@Client.on_message(filters.text & filters.incoming & filters.command("start@Aero_Force2_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("start@Aero_Force_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user.mention
	await msg.reply_photo(START_IMG,
		caption=Data.START,
		reply_markup=InlineKeyboardMarkup(Data.buttons)
                       )
