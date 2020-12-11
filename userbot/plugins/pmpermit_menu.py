"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio

from telethon import events, functions

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql

from . import PM_START, PMMESSAGE_CACHE, mention, set_key

PREV_REPLY_MESSAGE = {}


@bot.on(events.NewMessage(pattern=r"\/start", incoming=True))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if chat_id not in PM_START:
            PM_START.append(chat_id)
        if not event.is_private:
            return
        set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
        PM = (
            "Halo. Kamu mengakses menu yang tersedia di,"
            f"{mention}.\n"
            "__Beri tahu aku kenapa Kamu ada di sini.__\n"
            "**Pilih salah satu alasan berikut :**\n\n"
            "`A`. Untuk Mengobrol.\n"
            "`B`. Untuk Mengirim Spam Pesan.\n"
            "`C`. Untuk Menanyakan Sesuatu.\n"
            "`D`. Untuk Meminta Sesuatu.\n"
        )
        ONE = (
            "__Baik. Permintaan Kamu telah terdaftar. Jangan mengirim aku spam pesan. Mungkin Pesan Kamu akan mendapat balasan dalam waktu 24 tahun Lagi. Aku adalah orang yang sangat sibuk.__\n\n"
            "**⚠️ Kamu akan diblokir dan dilaporkan jika Kamu melakukan Spam Pesan. ⚠️**\n\n"
        )
        TWO = "**Sangat tidak baik. ini bukan rumahmu. Ganggu orang lain. Kamu telah diblokir dan dilaporkan hingga pemberitahuan lebih lanjut.**"
        THREE = "__Baik. Aku belum melihat pesan Kamu.__\n __Aku akan merespon ketika Sudah kembali, Banyak pesan yang tertunda juga.__\n **Harap jangan mengirim spam kecuali Kamu ingin diblokir dan dilaporkan.**"
        FOUR = "`Baik. mohon sopan santun agar tidak terlalu mengganggu ku. Jika Aku Sudah Kembali, Aku akan segera merespons Kamu.`\n**Jangan meminta berulang kali karena Kamu akan diblokir dan dilaporkan.**"
        LWARN = "**Ini peringatan terakhirmu. JANGAN kirim pesan lagi karena Anda akan diblokir dan dilaporkan. Tetap sabar. Aku akan membalas Anda secepat mungkin..**\n"
        try:
            async with event.client.conversation(chat) as conv:
                if pmpermit_sql.is_approved(chat_id):
                    return
                test1 = await event.client.send_message(chat, PM)
                set_key(PMMESSAGE_CACHE, event.chat_id, test1.id)
                chat_id = event.sender_id
                response = await conv.get_response(chat)
                y = response.text
                if y == "a" or "A":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test2 = await event.client.send_message(chat, ONE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test2.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test3 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test3.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test4 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test4.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "b" or "B":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test5 = await event.client.send_message(chat, LWARN)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test5.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test6 = await event.client.send_message(chat, TWO)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test6.id)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "c" or "C":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test7 = await event.client.send_message(chat, THREE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test7.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test8 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test8.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test9 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test9.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "d" or "D":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test10 = await event.client.send_message(chat, FOUR)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test10.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test11 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test11.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                else:
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    test12 = await event.client.send_message(
                        chat,
                        "Anda telah memasukkan perintah yang Salah. Silahkan kirim `/start` lagi atau jangan kirim pesan lain jika Anda tidak ingin diblokir dan dilaporkan.",
                    )
                    set_key(PMMESSAGE_CACHE, event.chat_id, test12.id)
                    response = await conv.get_response(chat)
                    z = response.text
                    if z != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test13 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test13.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test14 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test14.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
        except:
            pass
