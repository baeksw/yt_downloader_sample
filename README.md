# yt_downloader

유튜브 영상 다운로드 파이썬 패키지 샘플
 
## 사용 예시

```bash
# mp3로 저장
yt_downloader https://youtu.be/xxx --format mp3

# 720p 영상 저장
yt_downloader https://youtu.be/xxx --format 720p

# 다른 경로에 저장
yt_downloader https://youtu.be/xxx --output d:/downloads

yt_downloader https://www.youtube.com/playlist?list=xxxxxxxx --format best
yt_downloader https://youtu.be/xxxxxxx --format mp3

yt_downloader https://www.youtube.com/watch?v=xxxxxxx --format mp3 --output .
yt_downloader https://www.youtube.com/watch?v=xxxxxxx -f 720p -o downloads