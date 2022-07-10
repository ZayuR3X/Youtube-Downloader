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
    global link
    link = YouTube(input("Link\n----> "))
        
    stream = link.streams.filter(only_audio=True).first()


    print("İndiriliyor...") 
    
   
    output = stream.download("Müzikler2.0")
    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output,to_mp3)

    print ("-"*30)
    print("Audio Name: ",link.title)
    print ("Successfully")
    print ("-"*30)


while True:
        audio_download()

        """try:
            audio_download()
            yt = YouTube(link)
        except:                                         #video indikten sonra except çalışıyor...
            print("Hatalı Link\nProgram Kapanıyor...")
            exit()"""

        dongu = input("Devam edilsin mi? (y/n)  ")
        if dongu == "n":
            break
        elif dongu == "y":
            continue

        while dongu != ["y","n"]:
            print("y ve n seçeneği mevcuttur!!")
            dongu = input("Devam edilsin mi? (y/n)  ")
            if dongu == "y":
                break
            elif dongu == "n":
                break
        if dongu == "n": #for two
            break
        