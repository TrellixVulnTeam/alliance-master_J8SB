# Afk plugin from catuserbot ported from uniborg
import asyncio
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from ..utils import admin_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, mention

global USERTRX_ON
global trx_time
global last_trx_message
global trx_start
global trx_end
USERTRX_ON = {}
trx_time = None
last_trx_message = {}
trx_start = {}


@bot.on(admin_cmd(pattern=r"untrx ?(.*)", outgoing=True))
async def set_not_trx(event):
    if event.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    global USERTRX_ON
    global trx_time
    global last_trx_message
    global trx_start
    global trx_end
    back_alive = datetime.now()
    trx_end = back_alive.replace(microsecond=0)
    if trx_start != {}:
        total_trx_time = trx_end - trx_start
        time = int(total_trx_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        else:
            if h > 0:
                endtime += f"{h}h {m}m {s}s"
            else:
                endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message = event.message.message
    if "trx" not in current_message and "on" in USERTRX_ON:
        shite = await event.client.send_message(
            event.chat_id,
            "`Transaksi Selesai!`",
        )
        USERTRX_ON = {}
        trx_time = None
        await asyncio.sleep(5)
        await shite.delete()
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#TRXFALSE \n`Set TRX mode to False\n"
                + "Transaksi Selesai!`",
            )


@bot.on(
    events.NewMessage(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
)
async def on_trx(event):
    if event.fwd_from:
        return
    global USERTRX_ON
    global trx_time
    global last_trx_message
    global trx_start
    global trx_end
    global link
    back_alivee = datetime.now()
    trx_end = back_alivee.replace(microsecond=0)
    if trx_start != {}:
        total_trx_time = trx_end - trx_start
        time = int(total_trx_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        else:
            if h > 0:
                endtime += f"{h}h {m}m {s}s"
            else:
                endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message_text = event.message.message.lower()
    if "trx" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USERTRX_ON and not (await event.get_sender()).bot:
        msg = None
        if link and name:
            message_to_reply = (
                f"**{name}**"
            )
        elif reason:
            message_to_reply = (
                f"`{name}`"
            )
        else:
            message_to_reply = (
                f"`Sedang Transaksi`\n`Dari :` {endtime}\n`Dengan :` {name}\n`Ada apa? Sebentar ya?`"
            )
        if event.chat_id not in Config.UB_BLACK_LIST_CHAT:
            msg = await event.reply(message_to_reply)
        if event.chat_id in last_trx_message:
            await last_trx_message[event.chat_id].delete()
        last_trx_message[event.chat_id] = msg
        hmm = await event.get_chat()
        if Config.PM_LOGGR_BOT_API_ID:
            await asyncio.sleep(5)
            if not event.is_private:
                await event.client.send_message(
                    Config.PM_LOGGR_BOT_API_ID,
                    f"#TRANSAKSI \n<b>Group : </b><code>{hmm.title}</code>\
                            \n<b>Pesan : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>",
                    parse_mode="html",
                    link_preview=False,
                )


@bot.on(admin_cmd(pattern=r"trx ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    global USERTRX_ON
    global trx_time
    global last_trx_message
    global trx_start
    global trx_end
    global reason
    global link
    USERTRX_ON = {}
    trx_time = None
    last_trx_message = {}
    trx_end = {}
    start_1 = datetime.now()
    trx_start = start_1.replace(microsecond=0)
    if not USERTRX_ON:
        input_str = event.pattern_match.group(1)
        if ";" in input_str:
            msg, link = input_str.split(";", 1)
            reason = f"[{msg.strip()}]({link.strip()})"
            link = True
        else:
            reason = input_str
            link = False
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            trx_time = datetime.now()
        USERTRX_ON = f"on: {name}"
        if name:
            await edit_delete(event, f"{mention} `Sedang Transaksi Dengan >` {name}", 5)
        else:
            await edit_delete(event, f"{mention} `Sedang Transaksi!`", 5)
        if BOTLOG:
            if reason:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#TRANSAKSI \n{mention} `Sedang Transaksi Dengan >` {name}",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#TRANSAKSI \n{mention} `Sedang Transaksi!`",
                )


CMD_HELP.update(
    {
        "trx": "__**PLUGIN NAME :** Trx__\
\n\n📌** CMD ➥** `.trx` [Optional Reason]\
\n**USAGE   ➥  **Sets you as trx.\nReplies to anyone who tags/PM's \
you telling them that you are TRX(reason)\n\n__Switches off TRX when you type back anything, anywhere.__\
\n\n**Note :** If you want TRX with hyperlink use [ ; ] after reason, then paste the media link.\
\n**Example :** `.trx busy now ;<Media_link>`\
\n\n📌** CMD ➥** `.untrx`\
"
    }
)
