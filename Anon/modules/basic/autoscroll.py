# if you can read this, this meant you use code from Anon Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Anon doesn't care about credit
# at least we are know as well
# who Anon is
#
#
# ©2023 Anon Team
from pyrogram import filters, Client
from pyrogram.types import Message

from Anon.modules.basic import add_command_help
from Anon import cmds
the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])

if f:
   @Client.on_message(f)
   async def auto_read(bot: Client, message: Message):
       await bot.read_history(message.chat.id)
       message.continue_propagation()


@Client.on_message(filters.command("autoscroll", cmds) & filters.me)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


add_command_help(
    "autoscroll",
    [
        [f"{cmds}autoscroll",f"Send {cmds}autoscroll in any chat to automatically read all sent messages until you call "
            "autoscroll again. This is useful if you have Telegram open on another screen.",
        ],
    ],
)
