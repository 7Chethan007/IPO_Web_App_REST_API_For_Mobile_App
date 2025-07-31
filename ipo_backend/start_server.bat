@echo off
cls
echo ========================================
echo 🚀 IPO Management System - QUICK START
echo ========================================
echo.

echo ✅ Your Django REST API Server is Starting...
echo.
echo 📋 Available URLs:
echo   • API Overview: http://127.0.0.1:8000/api/
echo   • All IPOs: http://127.0.0.1:8000/api/ipos/
echo   • All Companies: http://127.0.0.1:8000/api/companies/
echo   • Search IPOs: http://127.0.0.1:8000/api/ipos/search/?q=tech
echo.
echo 🔐 For Admin Features:
echo   1. Create superuser: python manage.py createsuperuser
echo   2. Login at: http://127.0.0.1:8000/api/auth/login/
echo.
echo 📚 Documentation:
echo   • Quick Guide: TESTING_GUIDE.md
echo   • PostgreSQL Setup: POSTGRESQL_SETUP.md
echo   • Complete Summary: FINAL_SUMMARY.md
echo.
echo ========================================
echo Server starting... Press Ctrl+C to stop
echo ========================================
echo.

python manage.py runserver
