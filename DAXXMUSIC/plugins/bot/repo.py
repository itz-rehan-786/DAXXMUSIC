from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

✦ ɪ ᴀᴍ lund lele repo lega

✦ ᴛʜɪs ɪs ɴʏᴋᴀᴀ ᴍᴜsɪᴄ ʙᴏᴛ ᴏғғɪᴄɪᴀʟ ʀᴇᴘᴏ.

✦ ɪғ ʏᴏᴜ ᴡᴀɴᴛ teri maa ki chut laude 🌚🖕**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/dragons_society"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/chacha_vhidhayak"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/33bc093c89898dcc318ae.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
