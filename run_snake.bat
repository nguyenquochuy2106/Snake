@echo off
REM --- Kích hoạt virtual environment ---
call .venv\Scripts\activate.bat

REM --- Chạy main.py ---
python main.py

REM --- Tắt virtual environment khi thoát ---
deactivate

pause
