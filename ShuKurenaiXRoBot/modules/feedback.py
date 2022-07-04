import random

from telegram import ParseMode
from telethon import Button

from ShuKurenaiXRoBot import OWNER_ID, SUPPORT_CHAT
from ShuKurenaiXRoBot import telethn as tbot
from ShuKurenaiXRoBot.events import register

SHU1 = ( "https://telegra.ph/file/bfa2a4c3a59659e1d3900.jpg", 
      "https://telegra.ph/file/5295e906adbecf0b0d57c.jpg", 
      "https://telegra.ph/file/11992771e03bc607622a5.jpg", 
      "https://telegra.ph/file/b2f07deb75997d7657315.jpg", 
      "https://telegra.ph/file/4289b6a13927d27142d0e.jpg", 
      "https://telegra.ph/file/ad381e58b667455105b5e.jpg",  
      ) 
SHU2 = "https://telegra.ph/file/bcdc69ffbd6e4fa5bb6f8.jpg"

@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    BUTTON = [[Button.url("Go To Support Group", f"https://t.me/{SUPPORT_CHAT}")]]
    TEXT = "Thanks For Your Feedback, I Hope You Happy With Our Service"
    GIVE = "Give Some Text For Feedback ✨"
    logger_text = f"""
**New Feedback**

**From User:** {mention}
**Username:** @{e.sender.username}
**User ID:** `{e.sender.id}`
**Feedback:** `{e.text}`
"""
    if e.sender_id != OWNER_ID and not quew:
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=SHU2,
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(SHU1),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(SHU1), buttons=BUTTON)

__help__ = """
 -COMING SOON 
"""

__mod_name__ = "-"
