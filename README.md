# IPO Web App & REST API For Mobile App

This report outlines the production-level software development tasks assigned to interns at Bluestock Fintech. The project involves developing an IPO web application and REST API for the Bluestock website/app and our clients' websites/apps.

## 🚀 Project Overview

A comprehensive IPO (Initial Public Offering) management system with:
- **Django REST API Backend** - Complete backend API with PostgreSQL database
- **React Frontend** - Modern web application for IPO listings and management
- **Admin Dashboard** - Full administrative interface for IPO management
- **JWT Authentication** - Secure user authentication and authorization
- **PostgreSQL Database** - Production-ready database configuration

## 📁 Project Structure

```
IPO_Web_App_REST_API_For_Mobile_App/
├── ipo_backend/                # Django REST API Backend
│   ├── ipo_project/           # Main Django project
│   │   ├── settings.py        # PostgreSQL configuration
│   │   ├── urls.py           # API routing
│   │   └── wsgi.py
│   ├── companies/             # Company management app
│   │   ├── models.py         # Company model
│   │   ├── serializers.py    # API serializers
│   │   ├── views.py          # API views
│   │   └── urls.py           # Company endpoints
│   ├── ipos/                  # IPO management app
│   │   ├── models.py         # IPO, IPODocument, IPONews models
│   │   ├── serializers.py    # API serializers
│   │   ├── views.py          # CRUD operations
│   │   └── urls.py           # IPO endpoints
│   ├── accounts/              # User authentication
│   │   ├── models.py         # User profile model
│   │   ├── serializers.py    # Auth serializers
│   │   └── views.py          # Auth endpoints
│   ├── requirements.txt       # Python dependencies
│   ├── .env                  # Environment configuration
│   └── manage.py             # Django management
└── ipo_apps/                  # React Frontend Application
    ├── src/
    │   ├── components/        # Reusable components
    │   │   ├── Admin/        # Admin dashboard components
    │   │   ├── Auth/         # Authentication forms
    │   │   └── Common/       # Shared components
    │   ├── pages/            # Application pages
    │   │   ├── Admin/        # Admin pages
    │   │   └── User/         # User pages
    │   └── services/         # API integration
    ├── public/               # Static assets
    └── package.json          # Node.js dependencies
```

## 🛠️ Technology Stack

### Backend (Django REST API)
- **Django 4.2.7** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL 17.5** - Database
- **JWT Authentication** - Secure token-based auth
- **CORS Headers** - Cross-origin support
- **Pillow** - Image processing
- **psycopg2-binary** - PostgreSQL adapter

### Frontend (React)
- **React 18** - Frontend framework
- **Tailwind CSS** - Styling framework
- **Axios** - HTTP client
- **React Router** - Navigation
- **Chart.js** - Data visualization

## 🗄️ Database Configuration

### PostgreSQL Setup
```sql
-- Database Configuration
Database: ipo_db
Username: ipo_user  
Password: IPO_Backend
Host: localhost
Port: 5432
```

### Database Models
- **Company** - Company information and details
- **IPO** - IPO listings with dates, pricing, and status
- **IPODocument** - Document attachments for IPOs
- **IPONews** - News and updates related to IPOs
- **User Profile** - Extended user information

## 🔧 Installation & Setup

### Backend Setup (Django)

1. **Navigate to backend directory:**
```bash
cd ipo_backend
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **PostgreSQL Database Setup:**
```sql
-- Run in PostgreSQL command line (psql)
CREATE DATABASE ipo_db;
CREATE USER ipo_user WITH PASSWORD 'IPO_Backend';
GRANT ALL PRIVILEGES ON DATABASE ipo_db TO ipo_user;
ALTER DATABASE ipo_db OWNER TO ipo_user;
GRANT ALL ON SCHEMA public TO ipo_user;
```

5. **Environment Configuration:**
Create `.env` file with:
```env
# Database Configuration - PostgreSQL
DB_NAME=ipo_db
DB_USER=ipo_user
DB_PASSWORD=IPO_Backend
DB_HOST=localhost
DB_PORT=5432

# Django Admin Superuser Credentials
# Username: chethan
# Password: Chethan@007

# Django Secret Key
SECRET_KEY=your-secret-key-here-change-in-production

# Debug Mode
DEBUG=True

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# JWT Settings
ACCESS_TOKEN_LIFETIME=60
REFRESH_TOKEN_LIFETIME=1440
```

6. **Run database migrations:**
```bash
python manage.py migrate
```

7. **Create sample data:**
```bash
python manage.py create_sample_data
```

8. **Create superuser:**
```bash
python manage.py createsuperuser
# Username: chethan
# Password: Chethan@007
```

9. **Start development server:**
```bash
python manage.py runserver
```

### Frontend Setup (React)

1. **Navigate to frontend directory:**
```bash
cd ipo_apps
```

2. **Install dependencies:**
```bash
npm install
```

3. **Start development server:**
```bash
npm start
```

## 🔗 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `POST /api/auth/logout/` - User logout

### Companies
- `GET /api/companies/` - List all companies
- `POST /api/companies/` - Create company
- `GET /api/companies/{id}/` - Company details
- `PUT /api/companies/{id}/` - Update company
- `DELETE /api/companies/{id}/` - Delete company

### IPOs
- `GET /api/ipos/` - List all IPOs
- `POST /api/ipos/` - Create IPO
- `GET /api/ipos/{id}/` - IPO details
- `PUT /api/ipos/{id}/` - Update IPO
- `DELETE /api/ipos/{id}/` - Delete IPO
- `GET /api/ipos/upcoming/` - Upcoming IPOs
- `GET /api/ipos/active/` - Active IPOs

### IPO Documents
- `GET /api/ipos/{id}/documents/` - IPO documents
- `POST /api/ipos/{id}/documents/` - Upload document

### IPO News
- `GET /api/ipos/{id}/news/` - IPO news
- `POST /api/ipos/{id}/news/` - Create news

## 🏃‍♂️ Running the Application

1. **Start PostgreSQL service**
2. **Start Django backend:**
```bash
cd ipo_backend
venv\Scripts\activate
python manage.py runserver
```

3. **Start React frontend:**
```bash
cd ipo_apps
npm start
```

4. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## 🔐 Admin Credentials

- **Username:** chethan
- **Password:** Chethan@007

## 📋 Sample Data

The system includes sample data with:
- 5 Companies (Tech Innovations, Green Energy Solutions, HealthCare Plus, FinTech Masters, EduTech Solutions)
- 5 IPOs with various statuses and pricing information
- Complete company profiles and IPO details

## 🚀 Deployment Considerations

### Production Settings
- Set `DEBUG=False` in production
- Use secure SECRET_KEY
- Configure proper CORS origins
- Set up SSL/HTTPS
- Use production-grade PostgreSQL instance
- Configure proper logging

### Environment Variables
Ensure all sensitive information is stored in environment variables:
- Database credentials
- Secret keys
- API keys
- Debug settings

## 🛡️ Security Features

- JWT-based authentication
- CORS protection
- SQL injection prevention (Django ORM)
- XSS protection
- CSRF protection
- Secure file upload handling

## 📊 Database Schema

### Companies Table
- id, name, description, sector, founded_date
- website, email, phone, address
- logo, status, created_at, updated_at

### IPOs Table
- id, company (FK), issue_size, price_range
- issue_type, listing_date, issue_open_date, issue_close_date
- minimum_investment, lot_size, status
- description, created_at, updated_at

### IPO Documents Table
- id, ipo (FK), title, document_type, file, uploaded_at

### IPO News Table
- id, ipo (FK), title, content, published_at, created_at

## 🤝 Contributing

This project is developed as part of Bluestock Fintech internship program. For contributions:

1. Follow coding standards
2. Write comprehensive tests
3. Update documentation
4. Follow git workflow best practices

## 📞 Support

For technical support and questions related to this IPO management system, contact the development team at Bluestock Fintech.

---

**Project Status:** ✅ **Complete with PostgreSQL Integration**  
**Last Updated:** July 31, 2025  
**Version:** 1.0.0IPO-Web-App-REST-API-For-Mobile-App
This report outlines the production-level software development tasks assigned to interns at Bluestock Fintech. The project involves developing an IPO web application and design REST API for the Bluestock website/app and our clients’ websites/apps. 
