# IPO Web App & REST API        -       Figma UI Click -> [👇](#upcoming-ipo-standalone-figma-website)

A complete web application for managing IPO (Initial Public Offering) data with Django backend and React frontend.

## 🎯 What This Project Does

This is a full-stack web application that helps users:
- View and search IPO listings
- Register new IPO offerings
- Manage company information
- Access admin dashboard with statistics
- Handle user authentication securely

## 🛠️ Built With

**Backend:**
- Django (Python web framework)
- PostgreSQL (Database)
- Django REST Framework (API)
- JWT Authentication (Security)

**Frontend:**
- React.js (User interface)
- CSS3 (Styling)
- JavaScript (ES6+)

## 📁 Project Structure

```
IPO_Web_App_REST_API_For_Mobile_App/
├── ipo_backend/           # Django API server
│   ├── companies/         # Company management
│   ├── ipos/             # IPO management
│   ├── authentication/   # User login/signup
│   └── manage.py         # Django commands
└── ipo_apps/             # React web app
    ├── src/
    │   ├── components/   # UI components
    │   ├── pages/        # Web pages
    │   └── services/     # API connections
    └── package.json      # Dependencies
```

## ⚡ Quick Start

### 1. Backend Setup

```bash
# Go to backend folder
cd ipo_backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt

# Setup database (PostgreSQL required)
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### 2. Frontend Setup

```bash
# Go to frontend folder
cd ipo_apps

# Install Node.js packages
npm install

# Start React app
npm start
```

### 3. Access the Application

- **Website**: http://localhost:3000
- **API**: http://127.0.0.1:8000/api/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🗄️ Database Setup

You need PostgreSQL installed on your computer.

**Create Database:**
```sql
CREATE DATABASE ipo_db;
CREATE USER ipo_user WITH PASSWORD 'IPO_Backend';
GRANT ALL PRIVILEGES ON DATABASE ipo_db TO ipo_user;
```

**Environment File (.env):**
```
DB_NAME=ipo_db
DB_USER=ipo_user
DB_PASSWORD=IPO_Backend
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
```

## 🔑 Login Credentials

**Admin Access:**
- Username: `chethan`
- Password: `Chethan@007`

**Or create your own account using the signup form.**

## 📊 Main Features

### For Everyone
- Browse IPO listings
- Search companies
- View IPO details and dates
- Filter by status (Upcoming, Open, Listed)

### For Admin Users
- Add new companies
- Register new IPOs
- View dashboard statistics
- Manage all IPO data
- Delete entries when needed

## 🔗 API Endpoints

**Authentication:**
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - Create account

**Companies:**
- `GET /api/companies/` - List companies
- `POST /api/companies/` - Add company

**IPOs:**
- `GET /api/ipos/` - List IPOs
- `POST /api/ipos/` - Add IPO
- `GET /api/ipos/upcoming/` - Upcoming IPOs

## 🧪 Testing the API

Use Postman or similar tools to test:

```bash
# Get all IPOs
GET http://127.0.0.1:8000/api/ipos/

# Login user
POST http://127.0.0.1:8000/api/auth/login/
{
    "username": "your_username",
    "password": "your_password"
}
```

## 📱 How to Use

1. **Start both servers** (backend and frontend)
2. **Visit** http://localhost:3000
3. **Sign up** for a new account or **login**
4. **Browse IPOs** on the homepage
5. **Access admin features** after login
6. **Add new IPOs** using the registration form

## 🔧 Common Issues

**Backend won't start?**
- Check PostgreSQL is running
- Verify database credentials in .env file
- Run `python manage.py migrate`

**Frontend won't start?**
- Check Node.js is installed
- Run `npm install` again
- Clear browser cache

**Can't login?**
- Create superuser: `python manage.py createsuperuser`
- Check username/password spelling
- Verify backend server is running

## 📚 What I Learned

During this project, I learned:
- Django framework and REST API development
- React.js frontend development
- PostgreSQL database management
- JWT authentication implementation
- Full-stack application deployment
- API integration between frontend and backend

## 🎯 Project Goals Achieved

✅ Built complete IPO management system  
✅ Implemented user authentication  
✅ Created admin dashboard  
✅ Integrated PostgreSQL database  
✅ Developed responsive frontend  
✅ Added search and filter functionality  
✅ Implemented CRUD operations for IPOs  

## 🔄 Future Improvements

- Add email notifications
- Implement file upload for documents
- Add more detailed IPO analytics
- Mobile app development
- Advanced filtering options

---

**Project Status:** Complete and Working  
**Development Time:** Summer Internship Project

---

# Upcoming IPO Standalone Figma Website

**Live Preview (GitHub Pages):**  
<a href="https://7Chethan007.github.io/IPO_Web_App_REST_API_For_Mobile_App/" target="_blank" rel="noopener">
  https://7Chethan007.github.io/IPO_Web_App_REST_API_For_Mobile_App/
</a>

**Figma Design (viewable by anyone):**  
<a href="https://www.figma.com/design/6R142sm1lVrd8JMMV7QMb2/IPO_StandAlone_Figma?node-id=0-1&t=us49OhM26ZDEpONI-1" target="_blank" rel="noopener">
  https://www.figma.com/design/6R142sm1lVrd8JMMV7QMb2/IPO_StandAlone_Figma?node-id=0-1&t=us49OhM26ZDEpONI-1
</a>

---
