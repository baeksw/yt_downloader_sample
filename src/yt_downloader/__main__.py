import sys
from .downloader import download_youtube_video

def main():
    if len(sys.argv) < 2:
        print("사용법: python -m yt_downloader [유튜브 URL]")
        sys.exit(1)
    url = sys.argv[1]
    print(f"다운로드 시작: {url}")
    path = download_youtube_video(url)
    print(f"다운로드 완료: {path}")

if __name__ == "__main__":
    main()
