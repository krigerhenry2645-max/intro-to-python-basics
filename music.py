import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['www.youtube.com/watch?v=R5BCk7bsrwU&list=RDR5BCk7bsrwU&start_radio=1'])