from pyrogram.types import InlineKeyboardButton
from Config import BOT_USERNAME

class Data:
        # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

📚Use below buttons to learn more !

•Made By [AerodynamicV1~🇮🇳](https://t.me/AerodynamicV1_OFFICIAL)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("[►👁️‍🗨️Tutorial◄]", url="https://youtu.be/flYDpr4Ox1c"),
            InlineKeyboardButton("[►How to Use❔◄]", callback_data="help")
        ],
        [
            InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/Fiewin_Prediction_KingMasterMind"),
            InlineKeyboardButton("[►About Me◄]", callback_data="about")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/Fiewin_Colour_Prediction_Winner"),
        InlineKeyboardButton("[►Update🔔◄]", url="https://t.me/AerodynamicV1_UPDATE")]
    ]
        
# Help Message
    HELP = """
𝟷) ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴀ ɢʀᴏᴜᴘ. 
𝟸) ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴀs ᴀᴅᴍɪɴ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ғᴏʀᴄᴇ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ. ɪᴛ ᴄᴀɴ ʙᴇ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ, ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ. 
𝟹) ᴜsᴇ /fsub chat_id /username ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ғᴜɴᴄᴛɪᴏɴᴀʟ. ᴜsᴇ /id ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴄʜᴀᴛ ɪᴅ.
 ᴇxᴀᴍᴘʟᴇ : /fsub -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 ᴏʀ /forcesubsribe -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 
𝟺) [ᴏᴘᴛɪᴏɴᴀʟ] ᴜsᴇ /settings ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs! 
𝟻) ʏᴏᴜ ᴀʀᴇ ɢᴏᴏᴅ ᴛᴏ ɢᴏ. ʟᴇᴀᴠᴇ ᴛʜᴇ ʀᴇsᴛ ᴛᴏ ᴍᴇ.

 ✨ ᴀᴠᴀɪʟᴀʙᴇ ᴄᴍᴅs ʙᴀʙʏ  ✨ 
/start -  sᴛᴀʀᴛ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ʙᴏᴛ 
/fsub - sᴇᴇ ᴄᴜʀʀᴇɴᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ 
/fsub chat_id/username- ғᴏʀᴄᴇ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ
/settings - ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs 
/id - ɢᴇᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪᴅ ᴏғ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ 
☞︎︎︎ ɴᴏᴛᴇ - ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ /forcesubsribe ɪɴsᴛᴇᴀᴅ ᴏғ /fsub
"""

# About Message
    ABOUT = """
🔰About This Bot🔰

This is Aero ✘ Force Subscriber~🇮🇳
A powerful Telegram subscribing bot to force users in your group to join a particular chat. 
────────────────────
★Network » @AerodynamicV1Botz
★Developer » @AerodynamicV1_OFFICIAL
★Update » @AerodynamicV1_UPDATE
★Tech Earning » @Fiewin_Prediction_KingMasterMind
★Support » @Fiewin_Colour_Prediction_Winner
★Free Promotion » @AerodynamicV1_Promotion
    """
