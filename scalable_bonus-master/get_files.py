import requests
import os
import urllib

f = open("filenames.csv", "r")

lines = f.readlines()

audio_names = []
for line in lines:
    audio_name = line.split(".")[0]
    print(audio_name)
    audio_names.append(audio_name)
f.close()

for i in audio_names:
    url = "https://cs7ns1.scss.tcd.ie/index.php?download=noresume_speed&shortname=bonus&myfilename=" + i + ".mp3"
    dir = os.getcwd() + '/audios'
    urllib.request.urlretrieve(url, dir + "/" + i + ".mp3")
    print(dir + "/" + i + ".mp3") 
