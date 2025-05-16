

import click
from .downloader import download_youtube_video


@click.command()
@click.argument("url")
@click.option("--format", "-f", "fmt", default="best", show_default=True,
              help="다운로드 포맷 (best/720p/mp3 등)")
@click.option("--output", "-o", default=".", show_default=True, help="저장 경로")
def main(url, fmt, output):
    """유튜브 영상 또는 플레이리스트 전체 다운로드"""
    click.echo(f"다운로드 시작: {url} (포맷: {fmt})")
    download_youtube_video(url, output_path=output, fmt=fmt)
    click.echo("다운로드 완료")


if __name__ == "__main__":
    main()
