import asyncio

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="unoob$"))
@bot.on(sudo_cmd(pattern="unoob$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(9)
    event = await edit_or_reply(event, "unnoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@bot.on(admin_cmd(pattern="menoob$"))
@bot.on(sudo_cmd(pattern="menoob$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(9)
    event = await edit_or_reply(event, "menoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 9])
        await asyncio.sleep(animation_interval)


@bot.on(admin_cmd(pattern="upro$"))
@bot.on(sudo_cmd(pattern="upro$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(8)
    event = await edit_or_reply(event, "upro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@bot.on(admin_cmd(pattern="mepro$"))
@bot.on(sudo_cmd(pattern="mepro$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(8)
    event = await edit_or_reply(event, "mepro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
    ]
    for i in animation_ttl:
        await event.edit(animation_chars[i % 8])
        await asyncio.sleep(animation_interval)


@bot.on(admin_cmd(pattern=f"quickheal$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"quickheal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "quickheal")
    animation_chars = [
        "`Mendownload File..`",
        "`File Berhasil diDownload....`",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nTugas: 01 dari 01 File Diperiksa...\n\nHasil: Tidak Ditemukan Virus...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
        await event.delete()


@bot.on(admin_cmd(pattern=f"sqh$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"sqh$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(11)
    event = await edit_or_reply(event, "sqh")
    animation_chars = [
        "`Mendownload File..`",
        "`File Berhasil diDownload....`",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nTugas: 01 dari 01 File Diperiksa...\n\nHasil: Tidak Ditemukan Virus...`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
        await event.delete()


@bot.on(admin_cmd(pattern=f"vquickheal$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"vquickheal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "vquickheal")
    animation_chars = [
        "`Mendownload File..`",
        "`File Berhasil diDownload....`",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nFile Scanned... 100%\n█████████████████████████ `",
        "`Pemeriksaan Kemanan Data\n\n\nBerlangganan: @okinio\nBerlaku Sampai: 22/12/2022\n\nTugas: 01 dari 01 File Diperiksa...\n\nHasil:⚠️Ditemukan Virus⚠️\nInfo Lebih Lanjut: Torzan, Spyware, Adware`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
        await event.delete()


@bot.on(admin_cmd(pattern=f"macos$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"macos$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "macos")
    animation_chars = [
        "`Connecting To Macintosh...`",
        "`Initiating Macintosh Login.`",
        "`Loading Macintosh... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Macintosh... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Macintosh... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Macintosh... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Macintosh... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Macintosh... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Macintosh... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Macintosh... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Macintosh`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"windows$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"windows$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "windows")
    animation_chars = [
        "`Connecting To Windows 10...`",
        "`Initiating Windows 10 Login.`",
        "`Loading Windows 10... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Windows 10... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Windows 10... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"linux$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"linux$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "linux")
    animation_chars = [
        "`Connecting To Linux...`",
        "`Initiating Linux Login.`",
        "`Loading Linux... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Linux... 89%\n█████████████████████▒▒▒▒ `",
        "`Loading Linux... 100%\n█████████████████████████ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"stock$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"stock$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "stock")
    animation_chars = [
        "`Connecting To Symbian OS...`",
        "`Initiating Symbian OS Login.`",
        "`Loading Symbian OS... 0%\n█████████████████████████ `",
        "`Loading Symbian OS... 3%\n█████████████████████▒▒▒▒ `",
        "`Loading Symbian OS... 9%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 23%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 39%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 69%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 89%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Loading Symbian OS... 100%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS`\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"os$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"os$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(7)
    event = await edit_or_reply(event, "os")
    animation_chars = [
        "`Memeriksa OS...`",
        "`Memeriksa OS......`",
        "__Os yang dimuat saat ini: Symbian OS__\n\n**Untuk Boot OS Lain, Gunakan Cara Berikut:**\n☑️ `.macos`\n☑️ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
        "__Os yang dimuat saat ini: Symbian OS__\n\n**Untuk Boot OS Lain, Gunakan Cara Berikut:**\n✅ `.macos`\n☑️ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
        "__Os yang dimuat saat ini: Symbian OS__\n\n**Untuk Boot OS Lain, Gunakan Cara Berikut:**\n✅ `.macos`\n✅ `.windows`\n☑️ `.linux`\n☑️ `.stock`",
        "__Os yang dimuat saat ini: Symbian OS__\n\n**Untuk Boot OS Lain, Gunakan Cara Berikut:**\n✅ `.macos`\n✅ `.windows`\n✅ `.linux`\n☑️ `.stock`",
        "__Os yang dimuat saat ini: Symbian OS__\n\n**Untuk Boot OS Lain, Gunakan Cara Berikut:**\n✅ `.macos`\n✅ `.windows`\n✅ `.linux`\n✅ `.stock`\n\nDeveloped By: @okinio",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


CMD_HELP.update(
    {
        "animation6": "__**PLUGIN NAME :** Animation6__\
\n\n📌** CMD ➥** `.unoob` | `.menoob` | `.upro` | `.mepro` | `.quickheal` | `.vquickheal` | `.macos` | `.windows` | `.linux` | `.stock` | `.os` \
\n\n**USAGE   ➥  **These are animation bruh..Try & check yourself\
"
    }
)
