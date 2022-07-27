# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 Hello, {}**\n
<i>I Am A File To Link Bot</i>\n
<i>Click On Help To Get More Information</i>\n"""

        HELP_TEXT = """🔰 **How To Use Me?** 🔰

<i>Send Me Any File Or Media From Telegram</i>
<i>And I Will Provide You A Direct Link To That File/Media</i>

**⚡️ Fast Download Links ⚡️**"""

        ABOUT_TEXT = """
<b>⚜ My Name : Peach🍑Bot</b>\n
<b>⚜ Username : @PeachLDRMBot</b>\n
<b>🔸 Version : 1.0</b>\n
<b>🔹 Last Updated : [ 04-Apr-22 ]</b>
"""

        stream_msg_text ="""
<u>✅** Link Successfully Generated **✅</u>\n
<b>📂 File Name :</b> {}\n
<b>📦 File Size :</b> {}\n
<b>📥 Download :</b> {}\n
<b>🖥 Watch :</b> {}"""

        ban_text="🚫Access denied🚫"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ]        
        ]
    )
