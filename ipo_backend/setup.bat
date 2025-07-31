@echo off
echo ==========================================
echo IPO Management System - One Click Setup!
echo ==========================================
echo.

echo Installing requirements...
pip install -r requirements.txt

echo.
echo Setting up database...
python manage.py migrate

echo.
echo Creating sample data...
python manage.py create_sample_data

echo.
echo ==========================================
echo Setup Complete! Your API is ready!
echo ==========================================
echo.
echo To start the server:
echo python manage.py runserver
echo.
echo Then visit: http://127.0.0.1:8000/api/
echo.
echo Create admin user with:
echo python manage.py createsuperuser
echo.
pause
