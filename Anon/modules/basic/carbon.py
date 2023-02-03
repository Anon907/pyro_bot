# if you can read this, this meant you use code from AnonProject
# this code is from somewhere else
# please dont hestitate to steal it
# because Anon doesn't care about credit
# at least we are know as well
# who Anon is
#
#
# ©2023 Anon Team
import asyncio
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.types import Message

from Anon import aiosession

from pyanon.helper.PyroHelpers import ReplyCheck

from Anon.modules.basic import add_command_help
from Anon import cmds

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@Client.on_message(filters.command("carbon", cmds) & filters.me)
async def carbon_func(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.edit_text("`Preparing Carbon . . .`")
    carbon = await make_carbon(text)
    await ex.edit("`Uploading . . .`")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()


add_command_help(
    "carbon",[
        [f"{cmds}carbon <reply>", "Membuat Gambar carbon dengan default setting."],
    ],
)
