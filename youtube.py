
from __future__ import unicode_literals
import youtube_dl
import os

# Read URL
var = raw_input("Enter URL: ")

# Select different directories
dir1 = "/home/connor/Documents/media"
dir2 = "./"
dir3 = "./"

# Read in directory selection
dir = raw_input("(1): " + dir1 + "\n(2): " + dir2 + "\n(3): " + dir3)

# Change directory
if dir == "1":
	print "dir1 selected\n"
	os.chdir(dir1)
elif dir == "2":
	print "dir2 selected\n"
	os.chdir(dir2)
elif dir == "3":
	print "dir3 selected\n"
	os.chdir(dir3)

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
