@echo off
REM PostgreSQL Database Setup Script for IPO Management System (Windows)
REM This script creates the database and user for the IPO management system

echo Setting up PostgreSQL database for IPO Management System...

REM Database configuration
set DB_NAME=ipo_db
set DB_USER=ipo_user
set DB_PASSWORD=strongpassword

echo Creating database and user...

REM Create database and user using psql
psql -U postgres -c "CREATE DATABASE %DB_NAME%;" 2>nul || echo Database %DB_NAME% might already exist
psql -U postgres -c "CREATE USER %DB_USER% WITH PASSWORD '%DB_PASSWORD%';" 2>nul || echo User %DB_USER% might already exist
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE %DB_NAME% TO %DB_USER%;"
psql -U postgres -c "ALTER USER %DB_USER% CREATEDB;"

echo.
echo Database setup completed!
echo.
echo Database Details:
echo - Database Name: %DB_NAME%
echo - Username: %DB_USER%
echo - Password: %DB_PASSWORD%
echo - Host: localhost
echo - Port: 5432
echo.
echo You can now run Django migrations:
echo python manage.py migrate

pause
