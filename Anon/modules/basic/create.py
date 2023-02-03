# if you can read this, this meant you use code from Anon Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Anon doesn't care about credit
# at least we are know as well
# who Anon is
#
#
# ©2023 Anon Team
from pyrogram import Client, filters
from pyrogram.types import Message

from Anon.modules.basic import add_command_help
from Anon import cmds

@Client.on_message(filters.command("create", cmds) & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit_text(
            message, f"**Type .help create if you need help**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.edit_text("`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await xd.edit(
            f"**Successfully Created Telegram Group: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await xd.edit(
            f"**Successfully Created Telegram Channel: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "create",
    [
        [f"{cmds}create ch", "membuat channel"],
        [f"{cmds}create gc", "membuat group"],
    ],
)
