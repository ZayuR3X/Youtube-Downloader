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
    global x
    x = YouTube(input("Link: "))
    print("İndiriliyor...")
    stream = x.streams.filter(only_audio=True).first()
    
    
   
    output = stream.download("Müzikler")
    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output,to_mp3)

    print ("-"*30)
    print("Audio Name: ",x.title)
    print ("Successfully")
    print ("-"*30)


while True:
    try:
        audio_download()
        x = YouTube(x)

    except:
        print("Hatalı link!")
        continue
    
    dongu = input("Devam edilsin mi? (y/n) ")
    if dongu == "y":
        continue
    
    elif dongu == "n":
        break