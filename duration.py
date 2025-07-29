import subprocess
import re

def duration(filepath):
    try:
        result = subprocess.run(
            ['ffmpeg', '-i', filepath],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        output = result.stderr
        match = re.search(r'Duration: (\d+):(\d+):(\d+)', output)
        if match:
            hours, minutes, seconds = map(int, match.groups())
            return hours * 3600 + minutes * 60 + seconds
    except:
        pass
    return 0
