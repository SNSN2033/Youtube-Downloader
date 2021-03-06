from __future__ import unicode_literals
import youtube_dl

ydl_opts = {'format': 'bestaudio/best',
            "nocheckcertificate": True,
            "outtmpl": "video/%(title)s.%(ext)s",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=qvBf6WBatk0'])