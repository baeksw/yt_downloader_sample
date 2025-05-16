@echo off
REM === Conda 가상환경 "cook" 활성화 ===
call conda activate cook

REM === 의존성 및 툴 설치 ===
python -m pip install -U pip
python -m pip install -U build pytest

REM === 패키지 빌드 ===
python -m build --wheel
IF %ERRORLEVEL% NEQ 0 (
    echo [FAIL] 빌드 실패!
    exit /b 1
)

REM === 패키지 재설치 ===
pip install --force-reinstall dist\yt_downloader-0.1.0.tar.gz
IF %ERRORLEVEL% NEQ 0 (
    echo [FAIL] 설치 실패!
    exit /b 1
)


pause
