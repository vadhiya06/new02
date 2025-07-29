import math
import time

async def progress_bar(current, total, message, start):
    now = time.time()
    diff = now - start

    if round(diff % 5.0) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        estimated_total_time = round(total / speed)
        estimated_remaining_time = estimated_total_time - elapsed_time

        progress_str = "[{0}{1}] {2:.2f}%\n".format(
            ''.join(["█" for _ in range(math.floor(percentage / 10))]),
            ''.join(["░" for _ in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2)
        )

        tmp = progress_str + f"\n⏳ Uploaded: {human_readable_size(current)} of {human_readable_size(total)}\n"
        tmp += f"⚡ Speed: {human_readable_size(speed)}/s\n"
        tmp += f"⏱️ ETA: {time_formatter(estimated_remaining_time)}"

        try:
            await message.edit_text(f"`{tmp}`")
        except:
            pass

def time_formatter(seconds):
    minutes, sec = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m {sec}s" if hours else (f"{minutes}m {sec}s" if minutes else f"{sec}s")

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
