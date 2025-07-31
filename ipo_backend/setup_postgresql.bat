@echo off
echo =========================================
echo 🐘 PostgreSQL Database Setup for IPO API
echo =========================================
echo.

echo Step 1: Creating PostgreSQL database and user...
echo.
echo Please enter the PostgreSQL superuser password when prompted.
echo (This is the password you set when installing PostgreSQL)
echo.

echo Creating database: ipo_db
echo Creating user: ipo_user
echo Password: strongpassword
echo.

psql -U postgres -c "CREATE DATABASE ipo_db;" 2>nul
if %errorlevel% equ 0 (
    echo ✅ Database 'ipo_db' created successfully
) else (
    echo ⚠️  Database 'ipo_db' might already exist
)

psql -U postgres -c "CREATE USER ipo_user WITH PASSWORD 'strongpassword';" 2>nul
if %errorlevel% equ 0 (
    echo ✅ User 'ipo_user' created successfully
) else (
    echo ⚠️  User 'ipo_user' might already exist
)

psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ipo_db TO ipo_user;"
echo ✅ Privileges granted to ipo_user

psql -U postgres -c "ALTER USER ipo_user CREATEDB;"
echo ✅ User ipo_user can now create databases

echo.
echo =========================================
echo 🎉 PostgreSQL Setup Complete!
echo =========================================
echo.
echo Database Details:
echo   Name: ipo_db
echo   User: ipo_user  
echo   Password: strongpassword
echo   Host: localhost
echo   Port: 5432
echo.
echo Next steps:
echo   1. Run: python manage.py migrate
echo   2. Run: python manage.py create_sample_data
echo   3. Run: python manage.py createsuperuser
echo   4. Run: python manage.py runserver
echo.
pause
