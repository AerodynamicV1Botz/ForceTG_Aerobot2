from pyrogram import Client, filters


@Client.on_message(filters.text & filters.incoming & filters.command("id"))
@Client.on_message(filters.text & filters.incoming & filters.command("id@Aero_Force2_Subscriber_Bot"))
@Client.on_message(filters.text & filters.incoming & filters.command("id@Aero_Force_Subscriber_Bot"))
async def id(_, msg):
    await msg.reply(f"Chat ID is : `{msg.chat.id}`", quote=True)
