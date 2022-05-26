@echo off
echo ========================================
echo Activate Virtual Environment env 
echo ========================================
call venv/Scripts/Activate.bat
python manage.py runserver 127.0.0.1:8000