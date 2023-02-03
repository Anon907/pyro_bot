# if you can read this, this meant you use code from Anon Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Anon doesn't care about credit
# at least we are know as well
# who Anon is
#
#
# ©2023 Anon Team
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyanon.helper.utility import get_arg
from Anon.modules.basic import add_command_help
from Anon import cmds

@Client.on_message(filters.me & filters.command(["q", "quotly"], cmds))
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**Please Reply to Message**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("`Making a Quote . . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create Quotly Sticker**")


add_command_help(
    "quotly",
    [
        [f"{cmds}q or {cmds}quotly",
            "membuat gambar quote."],
        [f"{cmds}q <warna> or {cmds}quotly <warna>",
            "Membuat gambar quote dengan warna background." ],
    ],
)
