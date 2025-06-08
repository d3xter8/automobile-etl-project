@echo off
cd /d D:\Docs\Automobile_BI
call venv\Scripts\activate.bat
python main.py >> etl_log.txt 2>&1
