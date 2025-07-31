#!/bin/bash

# PostgreSQL Database Setup Script for IPO Management System
# This script creates the database and user for the IPO management system

echo "Setting up PostgreSQL database for IPO Management System..."

# Database configuration
DB_NAME="ipo_db"
DB_USER="ipo_user"
DB_PASSWORD="strongpassword"

# Check if PostgreSQL is running
if ! pgrep -x "postgres" > /dev/null; then
    echo "PostgreSQL is not running. Please start PostgreSQL service first."
    echo "On Windows: Start PostgreSQL service from Services"
    echo "On macOS: brew services start postgresql"
    echo "On Linux: sudo systemctl start postgresql"
    exit 1
fi

echo "Creating database and user..."

# Create database and user
psql -U postgres -c "CREATE DATABASE $DB_NAME;" 2>/dev/null || echo "Database $DB_NAME might already exist"
psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';" 2>/dev/null || echo "User $DB_USER might already exist"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
psql -U postgres -c "ALTER USER $DB_USER CREATEDB;"

echo "Database setup completed!"
echo ""
echo "Database Details:"
echo "- Database Name: $DB_NAME"
echo "- Username: $DB_USER"
echo "- Password: $DB_PASSWORD"
echo "- Host: localhost"
echo "- Port: 5432"
echo ""
echo "You can now run Django migrations:"
echo "python manage.py migrate"
