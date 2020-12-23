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
    animation_interval = 5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "{mention} `Melakukan Transfer Dana kepada` {name}")
    animation_chars = [
                "`Menyambungkan Ke Server Dana...`",
                "`✅ Login Ke Dana Sukses.`",
                "`Proses Transfer Uang Ke` {name} | `0%`\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `4%`\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `8%`\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `20%`\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `36%`\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `52%`\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `84%`\n█████████████████████▒▒▒▒ ",
                "`Proses Transfer Uang Ke` {name} | `100%`\n██████████████████████████ ",
                f"`✅ Transaksi Sukses.`\n\n{mention} `Telah Mengirim Uang Sebesar 110$ Ke` {name} ",
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
