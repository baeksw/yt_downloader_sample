
import yt_dlp


def download_youtube_video(url: str, output_path: str = ".", fmt: str = "best"):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(playlist_title)s/%(title)s.%(ext)s",
        "format": fmt,
        "noplaylist": False,  # 플레이리스트 전체 다운로드 (yt-dlp 기본값)
        "ignoreerrors": True,  # 오류 발생 시 다음 영상 계속
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
        ydl.download([url])
