import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "My Boss"
PM_IMG = "https://telegra.ph/file/266a1d83d0ca0f9c30c25.jpg"
pm_caption = "**Synergy ɪꜱ Alive**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/SynergysupportOfficial)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/synergyOT)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [ᴍɪᴛ ʟɪᴄᴇɴꜱᴇ](https://github.com/Gym2105/Synergy/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [gym2105](https://github.com/silverhalobit)\n"
pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓\n ┃┃━┃┃━━━━┃┃━┃┃\n ┃┗━┛┃┏━━┓┃┃━┃┃\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━\n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓\n ┗┛━┗┛┗━━┛┗━┛┗━┛](https://t.me/synergyOT)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is alive.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
