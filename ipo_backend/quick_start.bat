@echo off
REM Quick Start Script for IPO Management System
REM This script sets up the development environment

echo ===================================
echo IPO Management System Setup
echo ===================================
echo.

echo Step 1: Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Step 2: Creating database migrations...
python manage.py makemigrations

echo.
echo Step 3: Setting up database (using SQLite for quick start)...
echo Creating SQLite database for development...
python manage.py migrate

echo.
echo Step 4: Creating superuser account...
echo Please create an admin account:
python manage.py createsuperuser

echo.
echo Step 5: Creating sample data...
python manage.py create_sample_data

echo.
echo ===================================
echo Setup Complete!
echo ===================================
echo.
echo Your IPO Management System is ready!
echo.
echo To start the development server:
echo python manage.py runserver
echo.
echo Then visit:
echo - API: http://localhost:8000/api/
echo - Admin: http://localhost:8000/admin/
echo.
echo For PostgreSQL setup, see README.md
echo.

pause
