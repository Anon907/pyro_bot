# if you can read this, this meant you use code from Anon Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Anon doesn't care about credit
# at least we are know as well
# who Anon is
#
#
# ©2023 Anon Team

import os
from pyrogram import filters, Client
from pyrogram.types import Message
from py_trans import Async_PyTranslator
from pyanon.helper.utility import get_arg
from Anon.modules.basic import *
from Anon import cmds

@Client.on_message(filters.command(["tr", "translate"], cmds) & filters.me)
async def pytrans_tr(_, message: Message):
  tr_msg = await message.edit("`Processing...`")
  r_msg = message.reply_to_message
  args = get_arg(message)
  if r_msg:
    if r_msg.text:
      to_tr = r_msg.text
    else:
      return await tr_msg.edit("`Membalas pesan yang berisi teks!`")
    # Checks if dest lang is defined by the user
    if not args:
      return await tr_msg.edit(f"`Tentukan bahasa tujuan!`!`")
    # Setting translation if provided
    else:
      sp_args = args.split(" ")
      if len(sp_args) == 2:
        dest_lang = sp_args[0]
        tr_engine = sp_args[1]
      else:
        dest_lang = sp_args[0]
        tr_engine = "google"
  elif args:
    # Splitting provided arguments in to a list
    a_conts = args.split(None, 2)
    # Checks if translation engine is defined by the user
    if len(a_conts) == 3:
      dest_lang = a_conts[0]
      tr_engine = a_conts[1]
      to_tr = a_conts[2]
    else:
      dest_lang = a_conts[0]
      to_tr = a_conts[1]
      tr_engine = "google"
  # Translate the text
  py_trans = Async_PyTranslator(provider=tr_engine)
  translation = await py_trans.translate(to_tr, dest_lang)
  # Parse the translation message
  if translation["status"] == "success":
    tred_txt = f"""
**Translation Engine**: `{translation["engine"]}`
**Translated to:** `{translation["dest_lang"]}`
**Translation:**
`{translation["translation"]}`
"""
    if len(tred_txt) > 4096:
      await tr_msg.edit("`Wah!! Teks yang Diterjemahkan terlalu panjang!, Tunggu sebentar, saya akan mengirimkannya sebagai file!`")
      tr_txt_file = open("translated.txt", "w+")
      tr_txt_file.write(tred_txt)
      tr_txt_file.close()
      await tr_msg.reply_document("ptranslated_NEXAUB.txt")
      os.remove("ptranslated.txt")
      await tr_msg.delete()
    else:
      await tr_msg.edit(tred_txt)

add_command_help(
    "translate",
    [
        [f"{cmds}tr", "Terjemahkan beberapa teks dengan memberikan teks atau membalas teks."],
    ],
)
