import yt_dlp

ydl_opts = {
    'format': 'bestvideo[height<=720][fps>30]+bestaudio/best[height<=720][fps>30]',
    'outtmpl': 'jahrein_GTA_V/%(title)s.%(ext)s',
    'playliststart': 1,
}
playlist_url = 'https://www.youtube.com/watch?v=28oFYSDLRvc&list=PLdhHNEWonUO6JVXxJ9UonwEPczjBFOZFO&index=6'
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])