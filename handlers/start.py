from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/ec6f7ebb2bcb456902712.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""**Hey, I'm 🔥 {bn} 🎵
⚜️I am Рⷬaͣᴛⷮrͬiͥcͨiͥaͣ Musicbot.
⚜️I Am an Advance And Powerful Telegram Groups Voice Chat Music Bot.
Note:- Add @patriciaXmusic and @patriciaXmusic_bot to your group and make an admin.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥HELP🔥", url="https://telegra.ph/MANUAL-04-30-4")
                  ],
                    
                   [
                    InlineKeyboardButton(
                        "🔥MUSIC-WORLD🔥", url="https://t.me/Drama_drive"
                    ),

                    InlineKeyboardButton(
                        "🔥SUPPORT🔥", url="https://t.me/patricia_support"
                    )
                ],
                  [ 
                    InlineKeyboardButton(
                        "😘 Assistant 😘", url="https://t.me/patriciaXmusic"
                    )],
                    
                      [ 
                    InlineKeyboardButton(
                        "🔥ADD ME🔥", url="https://t.me/patriciaXmusic_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**💜 Рⷬaͣᴛⷮrͬiͥcͨiͥaͣ is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡Update_channel⚡", url="https://t.me/patricia_updates")
                ]
            ]
        )
   )
