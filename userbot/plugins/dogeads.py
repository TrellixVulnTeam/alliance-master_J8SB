# created by @okinio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(outgoing=True, pattern="cbot_help$"))
@bot.on(sudo_cmd(outgoing=True, pattern="cbot_help$", allow_sudo=True))
async def dogeads(mycbot):
    await edit_or_reply(
        mycbot, "Semua perintah ada [disini](https://nekobin.com/pemutuzeri) "
    )


@bot.on(admin_cmd(pattern="cbot(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(outgoing=True, pattern="cbot(?: |$)(.*)", allow_sudo=True))
async def dogeads(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    if link in ("menu", "m"):
        link = "🏠 Menu"
    elif link in ("visit", "vst"):
        link = "🖥 Visit sites"
    elif link == ("message", "msg"):
        link = "🤖 Message bots"
    elif link in ("join", "jn"):
        link = "📣 Join chats"
    elif link in ("balance", "bl"):
        link = "💰 Balance"
    elif link in ("referal", "ref"):
        link = "🙌🏻 Referrals"
    elif link in ("setting", "set"):
        link = "⚙️ Settings"
    elif link == ("history", "hs"):
        link = "🕐 History"
    elif link in ("myads", "ads"):
        link = "📊 My ads"
    catevent = await edit_or_reply(event, "```Sedang mengirim hasil....```")
    async with event.client.conversation("@Dogecoin_click_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=715510199)
            )
            await conv.send_message(f"{link}")
            response = await response
        except YouBlockedUserError:
            await catevent.edit("```Unblock @Dogecoin_click_bot nya cok```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, response.message)
            await event.client.send_read_acknowledge(conv.chat_id)


CMD_HELP.update(
    {
        "adsbot": "__**PLUGIN NAME :** Adsbot__\
    \n\n📌** CMD ➥** `.cbot_help` \
    \n**USAGE   ➥  **untuk mendapatkan daftar perintah.\
    \n\n📌** CMD ➥** `.cbot <kode perintah>`\
    \n**USAGE   ➥  **Ketik .cbot_kode untuk mendapatkan respon.\
    \n\n**Contoh:** `.cbot bl` , ini perintah untuk memeriksa balance."
    }
)
