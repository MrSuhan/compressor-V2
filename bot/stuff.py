#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A Video Encoder Which Can Encode Videos in HEVC.\nIt Reduces Size of Videos \nIt will Encode video in 480p quality.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="t.me/Anime_listz"),
                Button.url("DEVELOPER", url="t.me/Anime_listz"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 A Video Encoder Bot**\n\n+This Bot will Encode Videos.\n+Easy to Use\n-This bot is Hosted in OKTETO so it will take a lot of time\nSo Be patience and Send videos One By One After Completing.\nDont Spam Bot."
    )


async def ihelp(event):
    await event.edit(
        "**🐠 A Video Encoder Bot**\n\n+This Bot will Encode Videos.\n+Easy to Use\n-This bot is Hosted in OKTETO so it will take a lot of time\nSo Be patience and Send videos One By One After Completing.\nDont Spam Bot.",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A Video Encoder Which Can Encode Videos in HEVC.\nIt Reduces Size of Videos \nIt will Encode video in 480p quality.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="t.me/Anime_listz"),
                Button.url("DEVELOPER", url="t.me/Anime_listz"),
            ],
        ],
    )
