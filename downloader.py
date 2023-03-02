import os
from pytube import YouTube

# "Müzikler" klasörünü oluştur
if not os.path.exists("Müzikler"):
    os.makedirs("Müzikler")

while True:
    # Kullanıcının indirmek istediği video URL'sini alın
    url = input("İndirmek istediğiniz YouTube video URL'sini girin (q: çıkış): ")

    if url == "q":
        break

    try:
        # YouTube video nesnesi oluşturun
        video = YouTube(url)

        # İndirme seçenekleri
        audio_stream = video.streams.filter(only_audio=True).first()

        # İndirme işlemi başlatın
        print(f"{video.title} indiriliyor...")

        audio_stream.download(output_path="Müzikler/")
        
        print(f"{video.title} indirildi.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
