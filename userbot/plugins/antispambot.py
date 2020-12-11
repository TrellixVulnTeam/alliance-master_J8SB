#    Copyright (C) 2020  sandeep.n(π.$)
# baning spmmers plugin for catuserbot by @sandy1709 and @mrconfused
# included both cas(combot antispam service) and spamwatch (need to add more feaututres)

from requests import get
from telethon import events
from telethon.errors import ChatAdminRequiredError
from telethon.tl.types import ChannelParticipantsAdmins

from ..utils import admin_cmd, edit_or_reply, is_admin, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, LOGS, spamwatch
from .sql_helper.gban_sql_helper import get_gbanuser, is_gbanned

if Config.ANTISPAMBOT_BAN:

    @bot.on(events.ChatAction())
    async def anti_spambot(event):
        if not event.user_joined and not event.user_added:
            return
        chat = event.chat_id
        user = await event.get_user()
        catadmin = await is_admin(bot, chat, bot.uid)
        if not catadmin:
            return
        catbanned = None
        adder = None
        ignore = None
        if event.user_added:
            try:
                adder = event.action_message.sender_id
            except AttributeError:
                return
        async for admin in event.client.iter_participants(
            event.chat_id, filter=ChannelParticipantsAdmins
        ):
            if admin.id == adder:
                ignore = True
                break
        if ignore:
            return
        if is_gbanned(user.id):
            catgban = get_gbanuser(user.id)
            if catgban.reason:
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) Telah tergbanned oleh mu Dengan alasan `{catgban.reason}`"
                )
            else:
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) Telah tergbanned oleh mu"
                )
            try:
                await bot.edit_permissions(chat, user.id, view_messages=False)
                catbanned = True
            except Exception as e:
                LOGS.info(e)
        if spamwatch and not catbanned:
            ban = spamwatch.get_ban(user.id)
            if ban:
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) terbanned oleh spamwatch Dengan alasan `{ban.reason}`"
                )
                try:
                    await bot.edit_permissions(chat, user.id, view_messages=False)
                    catbanned = True
                except Exception as e:
                    LOGS.info(e)
        if not catbanned:
            try:
                casurl = "https://api.cas.chat/check?user_id={}".format(user.id)
                data = get(casurl).json()
            except Exception as e:
                LOGS.info(e)
                data = None
            if data and data["ok"]:
                reason = (
                    f"[Terbanned oleh Combot Anti Spam](https://cas.chat/query?u={user.id})"
                )
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) terbanned oleh Combat anti-spam service(CAS) Dengan alasan {reason}"
                )
                try:
                    await bot.edit_permissions(chat, user.id, view_messages=False)
                    catbanned = True
                except Exception as e:
                    LOGS.info(e)
        if BOTLOG and catbanned:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#ANTISPAMBOT\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {event.chat.title} (`{event.chat_id}`)\n"
                f"**Reason :** {hmm.text}",
            )


@bot.on(admin_cmd(pattern="cascheck$"))
@bot.on(sudo_cmd(pattern="cascheck$", allow_sudo=True))
async def caschecker(cas):
    catevent = await edit_or_reply(
        cas,
        "`checking user banned cas(combot antispam service) disini, dan ini akan memakan banyak waktu......`",
    )
    text = ""
    chat = cas.chat_id
    try:
        info = await cas.client.get_entity(chat)
    except (TypeError, ValueError) as err:
        await cas.edit(str(err))
        return
    try:
        cas_count, members_count = (0,) * 2
        banned_users = ""
        async for user in cas.client.iter_participants(info.id):
            if banchecker(user.id):
                cas_count += 1
                if not user.deleted:
                    banned_users += f"{user.first_name}-`{user.id}`\n"
                else:
                    banned_users += f"Deleted Account `{user.id}`\n"
            members_count += 1
        text = "Warning! Ditemukan `{}` of `{}` user yang terbanned CAS:\n".format(
            cas_count, members_count
        )
        text += banned_users
        if not cas_count:
            text = "User tidak ditemukan CAS!"
    except ChatAdminRequiredError:
        await catevent.edit("`CAS check gagal: Diperlukan Hak admin`")
        return
    except BaseException:
        await catevent.edit("`CAS check gagal`")
        return
    await catevent.edit(text)


@bot.on(admin_cmd(pattern="spamcheck$"))
@bot.on(sudo_cmd(pattern="spamcheck$", allow_sudo=True))
async def caschecker(cas):
    text = ""
    chat = cas.chat_id
    catevent = await edit_or_reply(
        cas,
        "`checking user banned spamwatch disini, dan ini akan memakan banyak waktu.....`",
    )
    try:
        info = await cas.client.get_entity(chat)
    except (TypeError, ValueError) as err:
        await cas.edit(str(err))
        return
    try:
        cas_count, members_count = (0,) * 2
        banned_users = ""
        async for user in cas.client.iter_participants(info.id):
            if spamchecker(user.id):
                cas_count += 1
                if not user.deleted:
                    banned_users += f"{user.first_name}-`{user.id}`\n"
                else:
                    banned_users += f"Deleted Account `{user.id}`\n"
            members_count += 1
        text = "Warning! Ditemukan `{}` of `{}` users yang terbanned spamwatch:\n".format(
            cas_count, members_count
        )
        text += banned_users
        if not cas_count:
            text = "User tidak ditemukan spamwatch!"
    except ChatAdminRequiredError:
        await catevent.edit("`spamwatch check gagal: Diperlukan Hak admin`")
        return
    except BaseException:
        await catevent.edit("`spamwatch check gagal`")
        return
    await catevent.edit(text)


def banchecker(user_id):
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    return bool(data and data["ok"])


def spamchecker(user_id):
    ban = None
    if spamwatch:
        ban = spamwatch.get_ban(user_id)
    return bool(ban)


CMD_HELP.update(
    {
        "antispambot": "__**PLUGIN NAME :** Aantispambot__\
        \n\n📌** CMD ➥** `.cascheck`\
        \n**USAGE   ➥  **Searches for cas(combot antispam service) banned users in group and shows you the list\
        \n\n📌** CMD ➥** `.spamcheck`\
        \n**USAGE   ➥  **Searches for spamwatch banned users in group and shows you the list"
    }
)
