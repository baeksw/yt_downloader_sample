from yt_downloader.downloader import download_youtube_video

def test_download(tmp_path):
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    output = download_youtube_video(url, output_path=str(tmp_path))
    assert output.endswith(".mp4")
