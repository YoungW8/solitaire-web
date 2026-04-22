@echo off
cd /d "%~dp0"
echo Server started: http://localhost:8080
echo Press Ctrl+C to stop
python server.py
pause
