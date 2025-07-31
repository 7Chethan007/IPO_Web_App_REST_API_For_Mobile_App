# IPO Management System - Django REST API Backend

A comprehensive Django REST Framework backend for managing IPO (Initial Public Offering) data, featuring JWT authentication, PostgreSQL database, and RESTful APIs for both admin operations and public access.

## Features

### 🔐 Authentication & Authorization
- JWT-based authentication using SimpleJWT
- Admin-only endpoints for data management
- Public access to IPO listings without authentication
- User registration and profile management

### 🏢 Company Management
- Complete CRUD operations for companies
- Company details including sector, industry, website, etc.
- Automatic IPO statistics (total IPOs, upcoming IPOs)
- Admin-only creation/modification, public read access

### 📈 IPO Management
- Comprehensive IPO data model with all necessary fields
- Status tracking (Upcoming, Open, Closed, Listed, Withdrawn)
- Subscription details and performance metrics
- Date-based filtering and smart queries
- Featured and recommended IPO marking

### 📄 Document Management
- RHP (Red Herring Prospectus) and DRHP upload/download
- PDF document handling with secure file storage
- Document type categorization
- Admin-controlled document management

### 🔍 Advanced Features
- Full-text search across companies and IPOs
- Filtering by multiple criteria (status, board, sector, etc.)
- Pagination for large datasets
- CORS support for React frontend integration
- Comprehensive API documentation

## Technology Stack

- **Backend Framework**: Django 4.2.7
- **API Framework**: Django REST Framework 3.14.0
- **Database**: PostgreSQL
- **Authentication**: JWT (SimpleJWT)
- **File Storage**: Local file system (production-ready for S3)
- **CORS**: django-cors-headers for frontend integration

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- PostgreSQL 12 or higher
- Git

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ipo_backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. PostgreSQL Database Setup

#### Install PostgreSQL
- **Windows**: Download from [PostgreSQL Official Site](https://www.postgresql.org/download/windows/)
- **macOS**: `brew install postgresql`
- **Linux**: `sudo apt-get install postgresql postgresql-contrib`

#### Create Database and User
```sql
-- Connect to PostgreSQL as superuser
sudo -u postgres psql

-- Create database
CREATE DATABASE ipo_db;

-- Create user
CREATE USER ipo_user WITH PASSWORD 'strongpassword';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE ipo_db TO ipo_user;

-- Exit
\q
```

### 5. Environment Configuration

Create a `.env` file in the project root with the following configuration:

```env
# Database Configuration
DB_NAME=ipo_db
DB_USER=ipo_user
DB_PASSWORD=strongpassword
DB_HOST=localhost
DB_PORT=5432

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

### 6. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Create Sample Data (Optional)
```bash
python manage.py create_sample_data
```

### 9. Run Development Server
```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000/api/`

## API Endpoints

### Authentication Endpoints
- `POST /api/auth/login/` - Login and get JWT tokens
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/token/refresh/` - Refresh access token
- `GET /api/auth/profile/` - Get user profile (authenticated)

### Company Endpoints
- `GET /api/companies/` - List all companies (public)
- `POST /api/companies/` - Create company (admin only)
- `GET /api/companies/{id}/` - Get company details (public)
- `PUT /api/companies/{id}/` - Update company (admin only)
- `DELETE /api/companies/{id}/` - Delete company (admin only)
- `GET /api/companies/{id}/ipos/` - Get company's IPOs (public)

### IPO Endpoints
- `GET /api/ipos/` - List all IPOs (public)
- `POST /api/ipos/` - Create IPO (admin only)
- `GET /api/ipos/{id}/` - Get IPO details (public)
- `PUT /api/ipos/{id}/` - Update IPO (admin only)
- `DELETE /api/ipos/{id}/` - Delete IPO (admin only)

#### Special IPO Endpoints
- `GET /api/ipos/upcoming/` - Get upcoming IPOs
- `GET /api/ipos/open/` - Get currently open IPOs
- `GET /api/ipos/featured/` - Get featured IPOs
- `GET /api/ipos/search/?q={query}` - Search IPOs

#### Document Management
- `POST /api/ipos/{id}/upload_documents/` - Upload RHP/DRHP (admin only)
- `GET /api/ipos/{id}/download_rhp/` - Download RHP document (public)
- `GET /api/ipos/{id}/download_drhp/` - Download DRHP document (public)
- `DELETE /api/ipos/{id}/delete_documents/?type=rhp` - Delete documents (admin only)

### Filtering & Search

#### Query Parameters
- `?search={query}` - Full-text search
- `?status=UPCOMING` - Filter by IPO status
- `?board=MAIN` - Filter by board type
- `?is_featured=true` - Filter featured IPOs
- `?company__sector=Technology` - Filter by company sector
- `?ordering=-created_at` - Sort results

#### Special Filters
- `?filter_status=upcoming` - Smart date-based upcoming filter
- `?filter_status=open` - Currently open IPOs
- `?filter_status=closed` - Closed IPOs
- `?filter_status=listed` - Listed IPOs

## Authentication Usage

### Login
```javascript
POST /api/auth/login/
{
  "username": "your_username",
  "password": "your_password"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "is_staff": true
  }
}
```

### Using JWT Token
```javascript
// Include in request headers
Authorization: Bearer <access_token>
```

## Frontend Integration (React)

### CORS Configuration
The backend is configured to allow requests from `http://localhost:3000` by default. Update `CORS_ALLOWED_ORIGINS` in settings for production domains.

### API Client Example
```javascript
// API service example
const API_BASE_URL = 'http://localhost:8000/api';

const apiService = {
  // Get all IPOs
  getIPOs: async () => {
    const response = await fetch(`${API_BASE_URL}/ipos/`);
    return response.json();
  },

  // Login
  login: async (credentials) => {
    const response = await fetch(`${API_BASE_URL}/auth/login/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials)
    });
    return response.json();
  },

  // Create IPO (admin only)
  createIPO: async (data, token) => {
    const response = await fetch(`${API_BASE_URL}/ipos/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }
};
```

## Admin Panel

Access the Django admin panel at: `http://localhost:8000/admin/`

Features:
- Complete IPO and Company management
- User management
- Document upload interface
- Advanced filtering and search
- Bulk operations

## File Structure

```
ipo_backend/
├── ipo_project/              # Main project settings
│   ├── settings.py           # Django settings with DRF config
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── companies/               # Companies app
│   ├── models.py            # Company model
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   ├── admin.py             # Admin interface
│   └── urls.py              # Company URLs
├── ipos/                    # IPOs app
│   ├── models.py            # IPO, Document, News models
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views with advanced filtering
│   ├── admin.py             # Admin interface
│   └── urls.py              # IPO URLs
├── authentication/          # Authentication app
│   ├── views.py             # Custom JWT views
│   └── urls.py              # Auth URLs
├── media/                   # File uploads (PDFs, images)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── manage.py               # Django management script
```

## Production Deployment

### Environment Variables for Production
```env
DEBUG=False
SECRET_KEY=your-secure-production-secret-key
DB_HOST=your-production-db-host
DB_PASSWORD=your-secure-db-password
CORS_ALLOWED_ORIGINS=https://yourfrontend.com
```

### Additional Production Steps
1. Configure proper PostgreSQL settings
2. Set up static file serving (WhiteNoise or CDN)
3. Configure media file storage (AWS S3 recommended)
4. Set up SSL certificates
5. Configure logging
6. Set up backup systems

## Testing

Run the test suite:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## API Documentation

Visit `http://localhost:8000/api/` for a complete API overview with all available endpoints.

## Support

For support and questions, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
