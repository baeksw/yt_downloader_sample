import yt_dlp


def _progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        filename = d.get('filename', '파일명없음')
        print(
            f"\r[진행률] {filename} | {percent} | 속도: {speed} | 남은시간: {eta} ", end='', flush=True)
    elif d['status'] == 'finished':
        filename = d.get('filename', '파일명없음')
        print(f"\n[완료] {filename}")


def download_youtube_video(url: str, output_path: str = ".", fmt: str = "best"):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(playlist_title)s/%(title)s.%(ext)s",
        "format": fmt,
        "noplaylist": False,
        "ignoreerrors": True,
        "progress_hooks": [_progress_hook],  # 진행률 콜백 연결
    }
    if fmt == "mp3":
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            pass
