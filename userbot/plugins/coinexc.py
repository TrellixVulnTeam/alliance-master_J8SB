# created by @okinio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(outgoing=True, pattern="xc_help$"))
@bot.on(sudo_cmd(outgoing=True, pattern="xc_help$", allow_sudo=True))
async def dogeads(myxc):
    await edit_or_reply(
        myxc, "Semua perintah ada [disini](https://nekobin.com/pemutuzeri) "
    )


@bot.on(admin_cmd(pattern="xc(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(outgoing=True, pattern="xc(?: |$)(.*)", allow_sudo=True))
async def dogeads(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    if link in "":
        link = ""
    elif link in "":
        link = ""
    elif link == "":
        link = ""
    catevent = await edit_or_reply(event, "```Sedang melihat harga tukar koin....```")
    async with event.client.conversation("@CryptoConvBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178947289)
            )
            await conv.send_message(f"{link}")
            response = await response
        except YouBlockedUserError:
            await catevent.edit("```Unblock @CryptoConvBot nya cok```")
            return
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, response.message)
            await event.client.send_read_acknowledge(conv.chat_id)
            await message.delete(5)


CMD_HELP.update(
    {
        "adsbot": "__**PLUGIN NAME :** Adsbot__\
    \n\n📌** CMD ➥** `.xc_help` \
    \n**USAGE   ➥  **untuk mendapatkan daftar perintah.\
    \n\n📌** CMD ➥** `.xc <kode perintah>`\
    \n**USAGE   ➥  **Ketik .xc <coin> to <coin> untuk mendapatkan respon.\
    \n\n**Contoh:** `.xc 1 btc idr` , ini perintah untuk memeriksa balance."
    }
)
