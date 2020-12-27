import sys
from os import execl
from time import sleep

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, HEROKU_APP, bot


@bot.on(admin_cmd(pattern="restart$"))
@bot.on(sudo_cmd(pattern="restart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    await edit_or_reply(
        event,
        "**Bot sedang Restart.**\nNanti `.ping` lagi sekitar 1-2 menit untuk mengecek sudah online atau belum. Harap sabar saat melakukan restart",
    )
    await bot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)


@bot.on(admin_cmd(pattern="shutdown$"))
@bot.on(sudo_cmd(pattern="shutdown$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if HEROKU_APP is not None:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down"
            )
        await edit_or_reply(
            event, "`Shutdown bot ...Nanti Kamu Harus Menghidupkannya Manual`"
        )
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        await edit_or_reply(
            event,
            "`Set HEROKU_APP_NAME dan HEROKU_API_KEY untuk bisa di gunakan`",
        )
        await bot.disconnect()


@bot.on(admin_cmd(pattern="sleep( [0-9]+)?$"))
@bot.on(sudo_cmd(pattern="sleep( [0-9]+)?$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "Syntax: `.sleep time`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Kamu menentukan bot untuk tidur selama " + str(counter) + " detik",
        )
    event = await edit_or_reply(
        event, f"`ok, aku akan tertidur selama {counter} detik`"
    )
    sleep(counter)
    await event.edit("`Aku Terbangun..`")


CMD_HELP.update(
    {
        "power_tools": "**Plugin : **`power_tools`\
                \n\n**Syntax : **`.restart`\
                \n**Usage : **Restarts the bot !!\
                \n\n**Syntax : **'.sleep <seconds>\
                \n**Usage: **Userbots get tired too. Let yours snooze for a few seconds.\
                \n\n**Syntax : **`.shutdown`\
                \n**Usage : **To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use @hk_heroku_bot"
    }
)
