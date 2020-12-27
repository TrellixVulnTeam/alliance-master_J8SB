# thx to @r4v4n4
import asyncio

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP, mention


@bot.on(admin_cmd(pattern=r"tf (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"tf (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    animation_interval = 20
    animation_ttl = range(11)
    event = await edit_or_reply(event, f"{mention} `Transfer Saldo Dana ke` {name}")
    animation_chars = [
        "`Menyambungkan Ke Server Dana...`",
        f"`Login Ke Dana` {mention} ",
        f"`Proses Transfer Uang Ke` {name} | `0%`\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `4%`\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `8%`\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `20%`\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `36%`\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `52%`\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `84%`\n█████████████████████▒▒▒▒ ",
        f"`Proses Transfer Uang Ke` {name} | `100%`\n█████████████████████████ ",
        f"`✅ Transaksi Sukses.`\n{mention} `Telah Mengirim Saldo Dana Sebesar 110$ Ke` {name} ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=r"trx (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"trx (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    shite = await edit_or_reply(
        event, f"{mention} `Sedang Melakukan Transaksi Dengan` {name}"
    )
    await asyncio.sleep(120)
    await shite.delete()


@bot.on(admin_cmd(pattern=r"untrx (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"untrx (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    shite = await edit_or_reply(event, f"`Transaksi Dengan` {name} `Telah Selesai`")
    await asyncio.sleep(60)
    await shite.delete()


CMD_HELP.update(
    {
        "tf": "__**PLUGIN NAME :** tf__\
    \n\n📌** CMD ➥** `.tf` reply to a person\
"
    }
)
