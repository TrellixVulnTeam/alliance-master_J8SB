# thx to @r4v4n4
import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import ALIVE_NAME, CMD_HELP, mention

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@bot.on(admin_cmd(pattern=r"tf (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"tf (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "{DEFAULTUSER} Melakukan Transfer Uang...")
    animation_chars = [
                "`Menyambungkan Ke Server Rekening...`",
                "`✅ Login Ke Rekening` {DEFAULTUSER} `Sukses.`",
                "`Proses Transfer Uang Ke` {name} | `0%`\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `4%`\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `8%`\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `20%`\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `36%`\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `52%`\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `84%`\n█████████████████████▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `100%`\n██████████████████████████ ",
                f"`Proses Transfer Selesai...`\n\n{mention} `Telah Mengirim Uang Sebesar 110$ Ke` {name} \n\n`✅ Transaksi Sukses..`",
            ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])

CMD_HELP.update(
    {
        "tf": "__**PLUGIN NAME :** tf__\
    \n\n📌** CMD ➥** `.tf` reply to a person\
"
    }
)
