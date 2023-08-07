from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

📚Use below buttons to learn more !

•Made By [AerodynamicV1~🇮🇳](https://telegram.me/AerodynamicV1_OFFICIAL)
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
            InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/AerodynamicV1_Promotion"),
            InlineKeyboardButton("[►About Me◄]", callback_data="about")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/AerodynamicV1_UPDATE/456"),
        InlineKeyboardButton("[►Update🔔◄]", url="https://t.me/AerodynamicV1_UPDATE")]
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub @AerodynamicV1_UPDATE` or `/forcesubscribe -1001212351472`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

     🔰**Available Commands**🔰

/fsub Or /forcesubscribe chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel

__**{►👁️‍🗨️ Watch Tutorial👉 [Click Here](https://youtu.be/flYDpr4Ox1c)◄}**__
    """


    # About Message
    ABOUT = """
**About This Bot** 

This is Aero ✘ Force Subscriber~🇮🇳
A powerful Telegram subscribing bot to force users in your group to join a particular chat. 
────────────────────
★Network » @AerodynamicV1Botz
★Developer » @AerodynamicV1_OFFICIAL
★Update » @AerodynamicV1_UPDATE
★Support » @AerodynamicV1_SUPPORT
★Free Promotion » @AerodynamicV1_Promotion
    """
