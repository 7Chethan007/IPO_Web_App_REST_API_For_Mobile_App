@echo off
echo 🚀 IPO Backend Quick Start
echo ========================
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Django development server...
echo Access at: http://localhost:8000
echo Admin panel: http://localhost:8000/admin
echo Username: admin
echo Password: admin123
echo.

python manage.py runserver 8000
