"""
imported from nicegrill
modified by @mrconfused
QuotLy: Avaible commands: .qbot
"""
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import CMD_HELP, process
from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def stickerchat(catquotes):
    if catquotes.fwd_from:
        return
    reply = await catquotes.get_reply_message()
    if not reply:
        await edit_or_reply(
            catquotes, "`tidak bisa mengutip pesan . reply ke sebuah pesan`"
        )
        return
    fetchmsg = reply.message
    repliedreply = await reply.get_reply_message()
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await edit_or_reply(catquotes, "`Format ini tidak support`")
        return
    catevent = await edit_or_reply(catquotes, "`Membuat quote...`")
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, catmsg = await process(fetchmsg, user, catquotes.client, reply, repliedreply)
    if not res:
        return
    catmsg.save("./temp/sticker.webp")
    await catquotes.client.send_file(
        catquotes.chat_id, "./temp/sticker.webp", reply_to=reply
    )
    await catevent.delete()
    os.remove("./temp/sticker.webp")


@bot.on(admin_cmd(pattern="qbot(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="qbot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply ke pesan user.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await edit_or_reply(event, "```Reply ke pesan teks```")
        return
    chat = "@QuotLyBot"
    catevent = await edit_or_reply(event, "```Membuat sebuah Quote```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await catevent.edit("```Tolong unblock (@QuotLyBot) dulu cok```")
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Hi!"):
            await catevent.edit(
                "``` Bisakah Kamu Menonaktifkan pengaturan privasi forward Kamu untuk selamanya?```"
            )
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "quotly": "__**PLUGIN NAME :** Quotly__\
        \n\n📌** CMD ➥** `.q` <reply to messge>`\
        \n**USAGE   ➥  **__Makes your message as sticker quote__\
        \n\n📌** CMD ➥** `.qbot` <reply to messge>\
        \n**USAGE   ➥  **__Makes your message as sticker quote by @quotlybot__\
        "
    }
)
