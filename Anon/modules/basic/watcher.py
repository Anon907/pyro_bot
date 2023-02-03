# if you can read this, this meant you use code from Anon Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Anon doesn't care about credit
# at least we are know as well
# who Anon is
#
#
# ©2023 Anon Team
import random
import asyncio
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import filters, Client
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import *
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from pyrogram import __version__
from pyanon.helper.utility import get_arg
from pyanon.helper.PyroHelpers import get_ub_chats
from pyanon.database.rraid import *
from cache.data import *
from Anon import SUDO_USER, cmds
from Anon.modules.basic import *
from Anon.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .spam import RAIDS



if RAIDS:
 @Client.on_message(filters.incoming)
 async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in BL_GCAST:
        return
    try:
        if message.from_user.id in (await get_rraid_users()):
            await message.reply_text(f"{random.choice(Anon)}")
    except AttributeError:
        pass
