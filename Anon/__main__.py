import importlib
import time
from pyrogram import idle
from uvloop import install
from pyanon import join
from pyanon import BOT_VER, __version__ as gver
from Anon import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR
from Anon.modules import ALL_MODULES


MSG_ON = """
**Anon Pyro Userbot**
**Userbot Version -** `{}`
**Anon Library Version - `{}`**
**Ketik** `{}anon` **untuk Mengecheck Bot**
©️2023 Anon Projects
"""
MSG_BOT = (f"**Anon Pyro Assistant**\nis alive...")




async def main():
    await app.start()
    LOGGER("Anon").info("LOG: Memulai Anon Pyro..")
    LOGGER("Anon").info("LOG: Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Anon.modules" + all_module)
        LOGGER("Anon").info(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
                await app.send_message(BOTLOG_CHATID, MSG_BOT)
            except BaseException as a:
                LOGGER("Anon").warning(f"{a}")
            LOGGER("Anon").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Anon").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Anon").info("Starting Anon Pyro Userbot")
    install()
    LOOP.run_until_complete(main())

