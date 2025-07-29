import os
import time
import subprocess
from pyrogram import Client
from pyrogram.types import Message
from plugins.progress import progress_bar
from plugins.duration import duration

async def send_doc(bot: Client, m: Message, cc, ka, cc1, prog, count, name):
    reply = await m.reply_text(f"<pre><code>Uploading » `{name}`</code></pre>")
    time.sleep(1)
    start_time = time.time()
    await m.reply_document(ka, caption=cc1)
    count += 1
    await reply.delete(True)
    time.sleep(1)
    os.remove(ka)
    time.sleep(3)

async def send_vid(bot: Client, m: Message, cc, filename, thumb, name, prog):
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
    await prog.delete(True)
    reply = await m.reply_text(f"**★彡 ᵘᵖˡᵒᵃᵈⁱⁿᵍ 彡★ ...⏳**\n\n📚𝐓𝐢𝐭𝐥𝐞 » `{name}`\n\n✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")

    try:
        thumbnail = f"{filename}.jpg" if thumb == "no" else thumb
    except Exception as e:
        await m.reply_text(str(e))
        return

    watermarked_filename = f"watermarked_{filename}"
    watermark_text = "SAINI BOTS"
    subprocess.run(
        f'ffmpeg -i "{filename}" -vf "drawtext=text='{watermark_text}':fontcolor=black@0.2:fontsize=24:x=(w-text_w)/2:y=(h-text_h)/2" -codec:a copy "{watermarked_filename}"',
        shell=True
    )

    dur = int(duration(watermarked_filename))
    start_time = time.time()

    try:
        await m.reply_video(
            watermarked_filename,
            caption=cc,
            supports_streaming=True,
            height=720,
            width=1280,
            thumb=thumbnail,
            duration=dur,
            progress=progress_bar,
            progress_args=(reply, start_time)
        )
    except Exception:
        await m.reply_document(
            watermarked_filename,
            caption=cc,
            progress=progress_bar,
            progress_args=(reply, start_time)
        )

    os.remove(watermarked_filename)
    os.remove(f"{filename}.jpg")
    await reply.delete(True)
