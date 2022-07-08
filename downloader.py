from pytube import YouTube
import os


"""link = input("Link: ")

directory = input("Directory: ")

try: 
    yt = YouTube(link) #link kontrol
except:
    print ("ınvalid Link !!!") #böyle bi link yok kanka
    exit()

mp3 = yt.streams.filter(only_audio=True).first()

print ("Donwloading...")

output = mp3.download(directory)

base, ext = os.path.splitext(output)
to_mp3 = base + ".mp3"
os.rename(output, to_mp3)

print ("Download Complate!")"""

def audio_download():
    x = YouTube(input("Link: "))
    stream = x.streams.filter(only_audio=True).first()
    stream.download()
    print ("-"*30)
    print ("Successfully")
    print("Audio Name: ",x.title)
    