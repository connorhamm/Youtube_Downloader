
from __future__ import unicode_literals
import youtube_dl
import os

var = raw_input("Enter URL: ")
print "\nDownloading to \"media\" folder"

os.chdir("/home/connor/Documents/media")
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([var])
