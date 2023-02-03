import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Anon.modules.basic import add_command_help
from Anon import cmds

@Client.on_message(filters.command(["dm"], cmds) & filters.me)
async def dm(xxx: Client, memek: Message):
    anon = await memek.reply_text("Proccessing.....")
    quantity = 1
    inp = memek.text.split(None, 2)[1]
    user = await xxx.get_chat(inp)
    spam_text = ' '.join(memek.command[2:])
    quantity = int(quantity)

    if memek.reply_to_message:
        reply_to_id = memek.reply_to_message.message_id
        for _ in range(quantity):
            await anon.edit("Pesan telah Terkirim")
            await xxx.send_message(user.id, spam_text,
                                      reply_to_messsge_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await xxx.send_message(user.id, spam_text)
        await anon.edit("Pesan telah Terkirim")
        await asyncio.sleep(0.15)


add_command_help(
    "DM",
    [
        [f"{cmds}dm @username", "Untuk Mengirim Pesan Tanpa Harus Kedalam Roomchat.",],
    ],
)
