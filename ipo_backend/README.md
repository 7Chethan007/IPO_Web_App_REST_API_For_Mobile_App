# IPO Web App - Backend API

A Django REST API for managing IPO (Initial Public Offering) data and user authentication.

## Project Overview

This backend provides APIs for:
- User authentication and registration
- IPO data management
- Company information management
- Admin dashboard statistics

## Technology Stack

- **Framework**: Django 4.2
- **API**: Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **CORS**: django-cors-headers

## Project Structure

```
ipo_backend/
├── ipo_project/          # Main Django project settings
├── authentication/      # User auth, login, signup APIs
├── companies/           # Company data models and APIs
├── ipos/               # IPO data models and APIs
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── .env               # Environment variables
```

## Database Setup

### PostgreSQL Configuration
1. Install PostgreSQL
2. Create database: `ipo_db`
3. Create user: `ipo_user` with password: `IPO_Backend`

### Environment Variables (.env)
```
DB_NAME=ipo_db
DB_USER=ipo_user
DB_PASSWORD=IPO_Backend
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## Installation & Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migration**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `GET /api/auth/profile/` - User profile
- `GET /api/auth/admin/stats/` - Admin dashboard stats

### Companies
- `GET /api/companies/` - List all companies
- `POST /api/companies/` - Create new company
- `GET /api/companies/{id}/` - Get company details
- `PUT /api/companies/{id}/` - Update company
- `DELETE /api/companies/{id}/` - Delete company (admin only)

### IPOs
- `GET /api/ipos/` - List all IPOs
- `POST /api/ipos/` - Create new IPO
- `GET /api/ipos/{id}/` - Get IPO details
- `PUT /api/ipos/{id}/` - Update IPO
- `DELETE /api/ipos/{id}/` - Delete IPO (admin only)
- `GET /api/ipos/upcoming/` - Get upcoming IPOs
- `GET /api/ipos/open/` - Get currently open IPOs

## Authentication

The API uses JWT (JSON Web Token) authentication. Include the token in the Authorization header:

```
Authorization: Bearer your_jwt_token_here
```

## Permissions

- **Public**: Can view IPO and company data
- **Authenticated Users**: Can create IPOs and companies
- **Admin Users**: Can delete IPOs and companies, access admin stats

## Sample Data

The project includes sample data for testing:
- 26 Companies across various sectors
- 31 IPOs with different statuses (Upcoming, Open, Listed)
- Multiple user accounts for testing

## Admin Panel

Access Django admin at: `http://127.0.0.1:8000/admin/`

## Testing

Test the API using:
- Postman collections
- Django admin interface
- Frontend application integration

## Common Issues

1. **Database Connection**: Ensure PostgreSQL is running
2. **CORS Issues**: Check CORS_ALLOWED_ORIGINS in settings
3. **JWT Tokens**: Tokens expire in 60 minutes by default

## Development Notes

- Backend runs on `http://127.0.0.1:8000/`
- API base URL: `http://127.0.0.1:8000/api/`
- Debug mode enabled for development
- Uses custom user authentication system