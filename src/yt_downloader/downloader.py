
import yt_dlp


def download_youtube_video(url: str, output_path: str = "."):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([url])
    return result
