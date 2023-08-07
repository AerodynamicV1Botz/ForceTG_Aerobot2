from ForceTG_Aerobot.database.users_sql import Users, num_users
from ForceTG_Aerobot.database.chats_sql import num_chats
from ForceTG_Aerobot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message
from Config import OWNER_ID

@Client.on_message( ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    chats = await num_chats()
    await msg.reply(f"ᴛᴏᴛᴀʟ ᴜsᴇʀs : {users} \n\nᴛᴏᴛᴀʟ ᴄʜᴀᴛs : {chats} \n\nʙᴏᴛ ᴜᴘᴅᴀᴛᴇ : @AerodynamicV1_Update", quote=True)
