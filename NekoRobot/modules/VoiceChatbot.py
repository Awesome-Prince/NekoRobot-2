 
import os
import aiofiles
import aiohttp
from random import randint
from pyrogram import filters
from NekoRobot import pbot as Neko


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data


async def ai_Neko(url):
    ai_name = "Neko.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@Neko.on_message(filters.command("voice"))
async def Asuna(_, message):
    if len(message.command) < 2:
        await message.reply_text("Neko AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    Asuna = text.replace(" ", "%20")
    m = await message.reply_text("Neko Is Best...")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=@NekoXRobot&ownername=@Horimaya"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "neko"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @Horimaya...")
    NekoVoice = await ai_Neko(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=NekoVoice, title=chatbot, performer=name)
    os.remove(NekoVoice)
    await m.delete()
