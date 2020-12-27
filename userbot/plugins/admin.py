# Userbot module to help you manage a group

# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

from asyncio import sleep

from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights, MessageMediaPhoto

from ..utils import admin_cmd, edit_or_reply, errors_handler, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, LOGS, get_user_from_event
from .sql_helper.mute_sql import is_muted, mute, unmute

# =================== CONSTANT ===================

PP_TOO_SMOL = "`Gambar Terlalu Kecil.!`"
PP_ERROR = "`Gagal Memproses Gambar`"
NO_ADMIN = "`Kamu Bukan Admin.! #sadcok`"
NO_PERM = "`Kamu Siapa? Bukan Admin Disini.`#sadcok"
CHAT_PP_CHANGED = "`Gambar Berhasil Diganti`"
INVALID_MEDIA = "`Inpalid, Coba Periksa Lagi..`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================


@bot.on(admin_cmd(pattern="setgpic$"))
@bot.on(sudo_cmd(pattern="setgpic$", allow_sudo=True))
@errors_handler
async def set_group_photo(gpic):
    if gpic.fwd_from:
        return
    if not gpic.is_group:
        await edit_or_reply(gpic, "`Ganti Photo Grup Dulu ah...`")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await edit_or_reply(gpic, NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await edit_or_reply(gpic, INVALID_MEDIA)
    sandy = None
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await gpic.client.upload_file(photo))
            )
            await edit_or_reply(gpic, CHAT_PP_CHANGED)
            sandy = True
        except PhotoCropSizeSmallError:
            await edit_or_reply(gpic, PP_TOO_SMOL)
        except ImageProcessFailedError:
            await edit_or_reply(gpic, PP_ERROR)
        except Exception as e:
            await edit_or_reply(gpic, f"**Error Cok : **`{str(e)}`")
        if BOTLOG and sandy:
            await gpic.client.send_message(
                BOTLOG_CHATID,
                "#GROUPPIC\n"
                f"Group profile pic changed "
                f"CHAT: {gpic.chat.title}(`{gpic.chat_id}`)",
            )


@bot.on(admin_cmd(pattern="promote(?: |$)(.*)", command="promote"))
@bot.on(sudo_cmd(pattern="promote(?: |$)(.*)", command="promote", allow_sudo=True))
@errors_handler
async def promote(promt):
    if promt.fwd_from:
        return
    chat = await promt.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(promt, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    catevent = await edit_or_reply(promt, "`Promoting...`")
    user, rank = await get_user_from_event(promt)
    if not rank:
        rank = "Admin"
    if not user:
        return
    try:
        await promt.client(EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await catevent.edit("`Berhasil Diundang! Now gib Party`")
    except BadRequestError:
        await catevent.edit(NO_PERM)
        return
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID,
            "#PROMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}(`{promt.chat_id}`)",
        )


@bot.on(admin_cmd(pattern="demote(?: |$)(.*)", command="demote"))
@bot.on(sudo_cmd(pattern="demote(?: |$)(.*)", command="demote", allow_sudo=True))
@errors_handler
async def demote(dmod):
    if dmod.fwd_from:
        return
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(dmod, NO_ADMIN)
        return
    catevent = await edit_or_reply(dmod, "`Demoting...`")
    rank = "admin"
    user = await get_user_from_event(dmod)
    user = user[0]
    if not user:
        return
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await dmod.client(EditAdminRequest(dmod.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await catevent.edit(NO_PERM)
        return
    await catevent.edit("`Berhasil Di Pecat!`")
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID,
            "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)",
        )


@bot.on(admin_cmd(pattern="ban(?: |$)(.*)", command="ban"))
@bot.on(sudo_cmd(pattern="ban(?: |$)(.*)", command="ban", allow_sudo=True))
@errors_handler
async def ban(bon):
    if bon.fwd_from:
        return
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(bon, NO_ADMIN)
        return
    user, reason = await get_user_from_event(bon)
    if not user:
        return
    catevent = await edit_or_reply(bon, "`Kamu Nakal yaa..!`")
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await catevent.edit(NO_PERM)
        return
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await catevent.edit("`Error, Periksa lagi!`")
        return
    if reason:
        await catevent.edit(f"`{str(user.id)}` Dia DiBanned !!\ngara-gara: {reason}")
    else:
        await catevent.edit(f"`{str(user.id)}` Dia DiBanned !!")
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID,
            "#BAN\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)",
        )


@bot.on(admin_cmd(pattern="unban(?: |$)(.*)", command="unban"))
@bot.on(sudo_cmd(pattern="unban(?: |$)(.*)", command="unban", allow_sudo=True))
@errors_handler
async def nothanos(unbon):
    if unbon.fwd_from:
        return
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(unbon, NO_ADMIN)
        return
    catevent = await edit_or_reply(unbon, "`Hmm, Terpaksa Unban`")
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await catevent.edit("```Berhasil Di UnBanned.```")
        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID,
                "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)",
            )
    except UserIdInvalidError:
        await catevent.edit("`Error!, Siapa Dia Cok? Ga Kenal!`")


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@bot.on(admin_cmd(pattern="mute(?: |$)(.*)", command="mute"))
@bot.on(sudo_cmd(pattern="mute(?: |$)(.*)", command="mute", allow_sudo=True))
async def startmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Yah Error!")
        await sleep(3)
        await event.get_reply_message()
        userid = event.chat_id
        replied_user = await event.client(GetFullUserRequest(userid))
        chat_id = event.chat_id
        if is_muted(userid, chat_id):
            return await event.edit("Wah...Mute Dia Cok..!")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error Cok!\nnih Error nya " + str(e))
        else:
            await event.edit("Berhasil Di Mute.!\n**Kasihan Gabisa Chatting u.u**")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#PM_MUTE\n"
                f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)",
            )
    else:
        chat = await event.get_chat()
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == bot.uid:
            return await edit_or_reply(event, "Begok, Mau Mute diri sendiri? Hadeh -_-")
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(event, "Dia Udah Di Mute Cok..!")
        try:
            admin = chat.admin_rights
            creator = chat.creator
            if not admin and not creator:
                await edit_or_reply(event, "`Kamu Siapa? Bukan Admin Disini.`#sadcok ")
                return
            result = await event.client(
                functions.channels.GetParticipantRequest(
                    channel=event.chat_id, user_id=user.id
                )
            )
            try:
                if result.participant.banned_rights.send_messages:
                    return await edit_or_reply(
                        event,
                        "Dia Udah Di Mute Cok..!",
                    )
            except:
                pass
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "`Kamu Siapa? Gapunya Ijin Disini. #sadcok`",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "`Kamu Siapa? Bukan Admin Disini.`#sadcok "
                )
            try:
                mute(user.id, event.chat_id)
            except Exception as e:
                return await edit_or_reply(event, "Error Cok!\nnih Error nya " + str(e))
        except Exception as e:
            return await edit_or_reply(event, f"**Ada Error nih : **`{str(e)}`")
        if reason:
            await edit_or_reply(
                event,
                f"{user.first_name} Kena Mute Di {event.chat.title}\n"
                f"`Gara-gara:`{reason}",
            )
        else:
            await edit_or_reply(
                event, f"{user.first_name} Kena Mute Di {event.chat.title}"
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#MUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd(pattern="unmute(?: |$)(.*)", command="unmute"))
@bot.on(sudo_cmd(pattern="unmute(?: |$)(.*)", command="unmute", allow_sudo=True))
async def endmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("Yah Error..!")
        await sleep(3)
        userid = event.chat_id
        replied_user = await event.client(GetFullUserRequest(userid))
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("__Dia Tidak Di Mute Cok..!__\n")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error Cok!\nnih Error nya " + str(e))
        else:
            await event.edit("Berhasil di unmute\nUdah bisa bicara lagi sekarang cok")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNMUTE\n"
                f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)",
            )
    else:
        user = await get_user_from_event(event)
        user = user[0]
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client(
                    functions.channels.GetParticipantRequest(
                        channel=event.chat_id, user_id=user.id
                    )
                )
                try:
                    if result.participant.banned_rights.send_messages:
                        await event.client(
                            EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                        )
                except:
                    return await edit_or_reply(
                        event,
                        "Dia Tidak di Mute Cok..!",
                    )
        except Exception as e:
            return await edit_or_reply(event, f"**Ada error nih : **`{str(e)}`")
        await edit_or_reply(
            event, "Berhasil di unmute\nUdah bisa bicara lagi sekarang cok"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)",
            )


@bot.on(admin_cmd(pattern="pin($| (.*))", command="pin"))
@bot.on(sudo_cmd(pattern="pin($| (.*))", command="pin", allow_sudo=True))
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        chat = await msg.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_delete(msg, NO_ADMIN, 5)
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        return await edit_delete(msg, "`Reply Pesan untuk di pin.`", 5)
    options = msg.pattern_match.group(1)
    is_silent = False
    if options == "loud":
        is_silent = True
    try:
        await msg.client.pin_message(msg.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(msg, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(msg, f"`{str(e)}`", 5)
    await edit_delete(msg, "`Pinned Berhasil!`", 3)
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG and not msg.is_private:
        try:
            await msg.client.send_message(
                BOTLOG_CHATID,
                "#PIN\n"
                f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
                f"LOUD: {is_silent}",
            )
        except:
            pass


@bot.on(admin_cmd(pattern="unpin($| (.*))", command="unpin"))
@bot.on(sudo_cmd(pattern="unpin($| (.*))", command="unpin", allow_sudo=True))
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        chat = await msg.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await edit_delete(msg, NO_ADMIN, 5)
            return
    to_unpin = msg.reply_to_msg_id
    options = (msg.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        await edit_delete(
            msg, "`Reply Pesan Untuk di unpin atau bisa juga .unpin all`", 5
        )
        return
    if to_unpin and not options:
        try:
            await msg.client.unpin_message(msg.chat_id, to_unpin)
        except BadRequestError:
            return await edit_delete(msg, NO_PERM, 5)
        except Exception as e:
            return await edit_delete(msg, f"`{str(e)}`", 5)
    elif options == "all":
        try:
            await msg.client.unpin_message(msg.chat_id)
        except BadRequestError:
            return await edit_delete(msg, NO_PERM, 5)
        except Exception as e:
            return await edit_delete(msg, f"`{str(e)}`", 5)
    else:
        return await edit_delete(
            msg, "`Reply Pesan Untuk di unpin atau bisa juga .unpin all`", 5
        )
    await edit_delete(msg, "`Unpinned Berhasil!`", 3)
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG and not msg.is_private:
        try:
            await msg.client.send_message(
                BOTLOG_CHATID,
                "#UNPIN\n"
                f"**Admin : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{msg.chat.title}(`{msg.chat_id}`)\n",
            )
        except:
            pass


@bot.on(admin_cmd(pattern="kick(?: |$)(.*)", command="kick"))
@bot.on(sudo_cmd(pattern="kick(?: |$)(.*)", command="kick", allow_sudo=True))
@errors_handler
async def kick(usr):
    if usr.fwd_from:
        return
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(usr, NO_ADMIN)
        return
    user, reason = await get_user_from_event(usr)
    if not user:
        await edit_or_reply(usr, "`Member Tidak Ditemukan.`")
        return
    catevent = await edit_or_reply(usr, "`Mengeluarkan Member Grup...`")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        await catevent.edit(NO_PERM + f"\n{str(e)}")
        return
    if reason:
        await catevent.edit(
            f"`Dikeluarkan Dari Grup` [{user.first_name}](tg://user?id={user.id})`!`\nReason: {reason}"
        )
    else:
        await catevent.edit(
            f"`DiKeluarkan Dari Grup` [{user.first_name}](tg://user?id={user.id})`!`"
        )
    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID,
            "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}(`{usr.chat_id}`)\n",
        )


@bot.on(admin_cmd(pattern="iundlt$", command="iundlt"))
@bot.on(sudo_cmd(pattern="iundlt$", command="iundlt", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await event.client.get_admin_log(
            event.chat_id, limit=5, edit=False, delete=True
        )
        deleted_msg = "Pesan Yang Terhapus Tadi:"
        for i in a:
            deleted_msg += "\nini yang dihapus ->`{}`".format(i.old.message)
        await edit_or_reply(event, deleted_msg)
    else:
        await edit_or_reply(event, "`Siapa Kamu? Bukan Admin Di sini`")
        await sleep(3)
        try:
            await event.delete()
        except:
            pass


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CMD_HELP.update(
    {
        "admin": "__**PLUGIN NAME :** Admin__\
\n\n📌** CMD ➥** `.setgpic` <reply to image>\
\n**USAGE   ➥  **Changes the group's display picture\
\n\n📌** CMD ➥** `.promote` <username/reply> <custom rank (optional)>\
\n**USAGE   ➥  **Provides admin rights to the person in the chat.\
\n\n📌** CMD ➥** `.demote` <username/reply>\
\n**USAGE   ➥  **Revokes the person's admin permissions in the chat.\
\n\n📌** CMD ➥** `.ban` <username/reply> <reason (optional)>\
\n**USAGE   ➥  **Bans the person off your chat.\
\n\n📌** CMD ➥** `.unban` <username/reply>\
\n**USAGE   ➥  **Removes the ban from the person in the chat.\
\n\n📌** CMD ➥** `.mute` <username/reply> <reason (optional)>\
\n**USAGE   ➥  **Mutes the person in the chat, works on admins too.\
\n\n📌** CMD ➥** `.unmute` <username/reply>\
\n**USAGE   ➥  **Removes the person from the muted list.\
\n\n📌** CMD ➥** `.pin` <reply> or `.pin loud`\
\n**USAGE   ➥  **Pins the replied message in Group\
\n\n📌** CMD ➥** `.unpin` <reply> or `.unpin all`\
\n**USAGE   ➥  **Unpins the replied message in Group\
\n\n📌** CMD ➥** `.kick` <username/reply> \
\n**USAGE   ➥  **kick the person off your chat.\
\n\n📌** CMD ➥** `.iundlt`\
\n**USAGE   ➥  **display last 5 deleted messages in group."
    }
)
