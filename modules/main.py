import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


'''OWNER = int(os.environ.get("OWNER", 6938835589))
try: 
    ADMINS=[] 
    for x in (os.environ.get("ADMINS", "7168441486 6938835589").split()): 
        ADMINS.append(int(x)) 
except ValueError: 
        raise Exception("Your Admins list does not contain valid integers.") 
ADMINS.append(OWNER)'''


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**ℍɪɪ ɧąƈƙɛཞ.😎 \n\n  𝔾ɪᴠᴇ /hacker ℂᴏᴍᴍᴀɴᴅ ᴛᴏ 𝔻ᴏᴡɴʟᴀᴏᴅ 𝔽ʀᴏᴍ ᴀ 𝕋ᴇ𝕩ᴛ ғɪʟᴇ.⚡️\n**")


@bot.on_message(filters.command(["stop"]))
async def restart_handler(_, m):
    await m.reply_text("**ℝᴜᴋ 𝔾ʏᴀ😁😎**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["hacker"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('**ℍɪɪ ɧąƈƙɛཞ.😎 \n\n 𝕋𝕆 ᴅᴏᴡɴʟᴏᴀᴅ ᴀ ᴛxᴛ ғɪʟᴇ 𝕤ᴇɴᴅ ʜᴇʀᴇ ⚡️**')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**__Invalid file input.__**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n**𝕊ᴇɴᴅ 𝔽ʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤** **`1`**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝔼ɴᴛᴇʀ 𝔹ᴀᴛᴄʜ ℕᴀᴍᴇ🤔**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸\n\nℚᴜᴀʟɪᴛʏ तो बताओ 𝕃ɪᴋᴇ 𝟷𝟺𝟺ᴘ, 𝟸𝟺𝟶ᴘ, 𝟹𝟼𝟶ᴘ, 𝟺𝟾𝟶ᴘ, 𝟽𝟸𝟶ᴘ, 𝟷𝟶𝟾𝟶ᴘ**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    

    instructions = (
        "**Enter your name or send `df` to use default. 📝**\n\n"
        "📄 You can also specify a custom name to be used before the file extension:\n\n"
        " `[ɧąƈƙɛཞ](https://t.me/Nda8009), [ɧąƈƙɛཞ]`\n\n"
        "===========================\n"
    )           
    await editable.edit(instructions)
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text.strip()
    await input3.delete(True)
    
    if raw_text3.lower() == 'df':
        MR = '[ɧąƈƙɛཞ](https://t.me/Nda8009)'
        name_before_extention = '[ɧąƈƙɛཞ]'
    else:
        if ',' in raw_text3:
            user_name, custom_value = map(str.strip, raw_text3.split(',', 1))
            MR = user_name
            name_before_extention = custom_value 
        else:
            MR = raw_text3  
            name_before_extention = '[ɧąƈƙɛཞ]'
 
    await editable.edit("Now upload the **Thumbnail URL** or `df` for default otherwise send `no` 🖼️")
    input6 = await bot.listen(editable.chat.id)
    raw_text6 = input6.text.strip()
    if raw_text6.lower() == "df":
        thumb = "thumb.jpg" 
    elif raw_text6.startswith("http://") or raw_text6.startswith("https://"):
        try:
            response = requests.get(raw_text6)
            if response.status_code == 200:
                thumb_filename = "downloaded_thumbnail.jpg"
                with open(thumb_filename, 'wb') as f:
                    f.write(response.content)
                thumb = thumb_filename
            else:
                await editable.edit("❌ Failed to download the image.")
                thumb = "no"
        except Exception as e:
            await editable.edit(f"❌ Error downloading image: {str(e)}")
            thumb = "no"
    else:
        thumb = "no"
    await input6.delete(True)
    await editable.delete()        

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V


            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp.com' in url or 'tencdn' in url or 'cdn.classplusapp.com' in url:
                masterhdr = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ijc1NDQwIiwiZW1haWwiOiJ0dWxzaXJhajYxM0BnbWFpbC5jb20iLCJ0aW1lc3RhbXAiOjE3MjE1NzQzMzh9.2KP9tr80rqMtAxsZmYkviu_XeubgfD2ErwIwFfXKFGM','user-agent': 'Mobile-Android'}
                url =requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=masterhdr).json()['url']

            elif '/master.mpd' in url: 
                #headers are missing for the pw mpd url request you can add it by yourself
                headers = {
                    "Authorization" : "Bearer "    # add the pw Authorization token here 
                }               
                id =  url.split("/")[-2] 
                resp = requests.post('https://api.penpencil.xyz/v1/files/get-signed-cookie', headers=headers, json={'url': f"https://d1d34p8vz63oiq.cloudfront.net/" + id + "/master.mpd"}).json()
                policy = resp['data']
                url = "https://kashurtek.site?url=" + id + f"/hls/{raw_text2}/main.m3u8" + policy
             
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "@").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                cc = f'**[🎥] Video_ID : {str(count).zfill(3)}.**\n\n**𝑽𝒊𝒅𝒆𝒐 𝑵𝒂𝒎𝒆** : **{name1}** - ({res}) {name_before_extention}.mkv\n\n**𝑩𝒂𝒕𝒄𝒉 𝑵𝒂𝒎𝒆** : {raw_text0}\n\n**𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒅 𝑩𝒚 : {MR}**'
                cc1 = f'**[📁] File_ID : {str(count).zfill(3)}.**\n\n**𝑭𝒊𝒍𝒆 𝑵𝒂𝒎𝒆** : **{name1}** - {name_before_extention}.pdf\n\n**𝑩𝒂𝒕𝒄𝒉 𝑵𝒂𝒎𝒆** : {raw_text0}\n\n**𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒅 𝑩𝒚 : {MR}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"🐬"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » `{name}`\n**Link** » {url}\n\nYouTube Link Failed So you can Directly Watch on YouTube"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**ℂᴏᴍᴘʟᴇᴛᴇ ℍᴏ 𝔾ʏᴀ 𝔹ᴏ𝕤𝕤😎**")

bot.run()
