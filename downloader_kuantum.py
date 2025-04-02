import yt_dlp
ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'outtmpl': 'kuantum_fizigi/%(title)s.%(ext)s',
    'playliststart': 1,
}
playlist_url = 'https://www.youtube.com/watch?v=9fAu-LT_QNs&list=PLqNc_xpYGu74ITb-yC12eTM_skV6mtUen'
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])