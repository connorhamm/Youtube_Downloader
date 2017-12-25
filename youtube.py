
from __future__ import unicode_literals
import youtube_dl
import os

var = raw_input("Enter URL: ")
print "\nDownloading to \"media\" folder"

os.chdir("/home/connor/Documents/media")

x = raw_input("Select Format: (1) - audio (2) - audio+video\n")

if x == "1":
	print "audio selected\n"
	ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}
else:
	print "audio + video selected\n"
	ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([var])
