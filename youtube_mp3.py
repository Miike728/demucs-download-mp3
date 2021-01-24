#prerequisites: 
#ffmpeg and youtube-dl
#python youtube_mp3.py <youtube_url>


import youtube_dl
import sys

params ={
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
}

youtube= youtube_dl.YoutubeDL(params)
youtube.download(sys.argv[1:])
