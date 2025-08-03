# IPO Web App - Frontend

A React.js web application for managing and viewing IPO information with admin dashboard.

## Project Overview

This frontend application provides:
- User registration and authentication
- IPO listing and search functionality
- Admin dashboard with statistics
- IPO registration and management
- Responsive design for all devices

## Technology Stack

- **Framework**: React.js 18
- **Routing**: React Router DOM
- **Styling**: CSS3, Custom Components
- **HTTP Client**: Fetch API
- **Authentication**: JWT Token Management
- **Icons**: Custom icon components

## Project Structure

```
ipo_apps/
├── public/              # Static files
├── src/
│   ├── components/      # Reusable React components
│   │   ├── Auth/       # Login, Signup forms
│   │   ├── Admin/      # Admin dashboard components
│   │   └── Common/     # Shared components
│   ├── pages/          # Page components
│   ├── services/       # API service functions
│   ├── App.js          # Main application component
│   └── index.js        # Application entry point
├── package.json        # Dependencies and scripts
└── README.md          # This file
```

## Features

### Public Features
- View upcoming IPOs
- Search IPOs by company name
- Filter IPOs by status and board type
- Responsive design

### Admin Features
- User authentication (login/signup)
- Admin dashboard with statistics
- Register new IPOs
- Manage existing IPOs
- View all companies and IPO data

## Installation & Setup

1. **Install Node.js** (version 16 or higher)

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Environment Setup**
   Create `.env` file with:
   ```
   REACT_APP_API_URL=http://127.0.0.1:8000/api
   ```

4. **Start Development Server**
   ```bash
   npm start
   ```

5. **Open Browser**
   Navigate to: `http://localhost:3000`

## Available Scripts

- `npm start` - Run development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App

## Application Routes

### Public Routes
- `/` - Home page with IPO listings
- `/admin/signin` - Admin login page
- `/admin/signup` - Admin registration page

### Protected Routes (Admin)
- `/admin/dashboard` - Admin dashboard with stats
- `/admin/register-ipo` - IPO registration form
- `/admin/manage-ipo` - IPO management interface

## Authentication Flow

1. **Registration**: New users sign up with username, email, password
2. **Login**: Users login with username/email and password
3. **JWT Token**: Received token stored in localStorage
4. **Auto-redirect**: Successful login redirects to admin dashboard
5. **Token Validation**: API calls include JWT token in headers

## API Integration

The frontend connects to the Django backend API:

### Services
- `authService.js` - User authentication
- `ipoService.js` - IPO data management
- `companyService.js` - Company data management
- `apiClient.js` - HTTP client with JWT handling

### Sample API Calls
```javascript
// Get all IPOs
const ipos = await ipoService.getAllIPOs();

// Create new IPO
const newIPO = await ipoService.createIPO(ipoData);

// User login
const user = await authService.login(credentials);
```

## Styling

- Custom CSS for all components
- Responsive design principles
- Modern card-based layouts
- Professional color scheme
- Mobile-first approach

## Key Components

### Authentication
- `SigninForm.jsx` - User login form
- `SignupForm.jsx` - User registration form

### Admin Dashboard
- `Dashboard.jsx` - Main admin dashboard
- `DashboardOverview.jsx` - Statistics overview
- `RegisterIPOForm.jsx` - IPO creation form
- `ManageIPO.jsx` - IPO management interface

### Common Components
- `Navbar.jsx` - Navigation header
- `Sidebar.jsx` - Admin navigation sidebar
- `IPOCard.jsx` - IPO display card

## Data Management

- Local state management with React hooks
- JWT token persistence in localStorage
- Real-time data updates from backend API
- Form validation and error handling

## Testing Credentials

For testing purposes:
- **Admin User**: `chethan@admin.com` / `Chethan@007`
- **Regular User**: Create via signup form

## Common Issues

1. **CORS Errors**: Ensure backend CORS settings allow frontend URL
2. **API Connection**: Check backend server is running on port 8000
3. **Token Expiry**: Tokens expire after 60 minutes, login again
4. **Route Protection**: Some routes require admin authentication

## Development Notes

- Frontend runs on `http://localhost:3000`
- Backend API expected at `http://127.0.0.1:8000/api`
- Uses functional components with hooks
- Responsive design tested on mobile and desktop