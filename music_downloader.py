import os
import time
from pytubefix import YouTube, Playlist
from colorama import Fore, Style, init

# Colorama'yı terminal çıktısı için başlatıyoruz
init(autoreset=True)

def print_banner():
    banner = f""" 
    {Fore.RED}
    ██████╗ ██████╗ ██╗  ██╗                          
    ██╔══██╗╚════██╗╚██╗██╔╝                          
    ██████╔╝ █████╔╝ ╚███╔╝                           
    ██╔══██╗ ╚═══██╗ ██╔██╗                           
    ██║  ██║██████╔╝██╔╝ ██╗                          
    ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝                          
                                                    
    ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗███████╗██╗
    ████╗ ████║██║   ██║██╔════╝██║██╔════╝██╔════╝██║
    ██╔████╔██║██║   ██║███████╗██║██║     ███████╗██║
    ██║╚██╔╝██║██║   ██║╚════██║██║██║     ╚════██║╚═╝
    ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗███████║██╗
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝╚══════╝╚═╝
                    
                    Made by Ahmet 
                                                    
    {Style.RESET_ALL}
    """
    print(banner)

def download_song(url):
    try:
        if not url:
            raise ValueError (f"{Fore.RED}Geçerli bir URL girilmedi. Lütfen bir URL girdiğinizden emin olun.")
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
    
        # Dosya adını oluştur
        filename = f"{yt.title}.mp3"
    
        # İndirme işlemini başlat
        print(f"{Fore.YELLOW}İndirme başlatılıyor: '{yt.title}'...")

        # İndirme işlemi
        stream.download(output_path='downloads', filename=filename)

        print(f"{Fore.GREEN}✓ '{yt.title}' başarıyla indirildi!")
    
    except Exception as e:
        print(f"{Fore.RED}Hata: {e}")
        print(f"{Fore.RED}Lütfen geçerli bir URL girin.")

def download_playlist(playlist_url):
    try:
        if not playlist_url:
            raise ValueError (f"{Fore.RED}Geçerli bir URL girilmedi. Lütfen bir URL girdiğinizden emin olun.")
        playlist = Playlist(playlist_url)
        for video in playlist.videos:
            stream = video.streams.filter(only_audio=True).first()
            filename = f"{video.title}.mp3"
        
            print(f"{Fore.YELLOW}İndirme başlatılıyor: '{video.title}'...")

            # İndirme işlemi
            stream.download(output_path='downloads', filename=filename)

            print(f"{Fore.GREEN}✓ '{video.title}' başarıyla indirildi!")
    
    except Exception as e:
        print(f"{Fore.RED}Hata: {e}")
        print(f"{Fore.RED}Lütfen geçerli bir URL girin.")

if __name__ == "__main__":
    print_banner()
    while True:
        time.sleep(0.5)
        choice = input(f"{Fore.CYAN}Şarkı indirmek için '1'\nÇalma listesi indirmek için '2'\nÇıkmak için 'q' yazın\n---->  ")
        if choice == '1':
            song_url = input(f"{Fore.CYAN}İndirmek istediğiniz şarkının URL'sini girin (Çıkmak için 'q'): ")
            if song_url == 'q':
                time.sleep(0.5)
                print(f"{Fore.RED}Programdan çıkılıyor...")
                time.sleep(0.5)
                break    
            download_song(song_url)
        elif choice == '2':
            playlist_url = input(f"{Fore.CYAN}İndirmek istediğiniz çalma listesinin URL'sini girin (Çıkmak için 'q'): ")
            if playlist_url == 'q':
                time.sleep(0.5)
                print(f"{Fore.RED}Programdan çıkılıyor...")
                time.sleep(0.5)
                break
            download_playlist(playlist_url)
        elif choice.lower() == 'q':
            time.sleep(0.5)
            print(f"{Fore.RED}Programdan çıkılıyor...")
            time.sleep(0.5)
            break
        else:
            print(f"{Fore.RED}Geçersiz seçim. Lütfen tekrar deneyin.")

# pyinstaller --onefile music_downloader.py