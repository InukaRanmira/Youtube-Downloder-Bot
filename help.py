from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/sl_bot_zone")
      ],
      [ 
        InlineKeyboardButton(
            "Support Group", url="https://t.me/slbotzone")]
    ])  
    helptxt = f"<b> Just send a Youtube url to download it in video or audio format!\n\n ~ @InukaRanmira </b>"
    await message.reply_text(helptxt, reply_markup=joinButton)
