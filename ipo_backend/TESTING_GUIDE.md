# 🧪 API Testing Guide - Super Simple!

## 🚀 Your API is Running at: http://127.0.0.1:8000/

---

## 📋 **Test These URLs in Your Browser Right Now!**

### **1. API Overview**
```
http://127.0.0.1:8000/api/
```
*Shows all available endpoints*

### **2. View All IPOs**
```
http://127.0.0.1:8000/api/ipos/
```
*See all 5 sample IPOs with company info*

### **3. View All Companies**
```
http://127.0.0.1:8000/api/companies/
```
*See all 5 sample companies*

### **4. Get Upcoming IPOs**
```
http://127.0.0.1:8000/api/ipos/upcoming/
```
*See IPOs opening soon*

### **5. Search for Tech IPOs**
```
http://127.0.0.1:8000/api/ipos/search/?q=tech
```
*Find IPOs with "tech" in name*

### **6. Get Company Details**
```
http://127.0.0.1:8000/api/companies/1/
```
*Detailed info about first company*

### **7. Get IPO Details**
```
http://127.0.0.1:8000/api/ipos/1/
```
*Full details of first IPO*

---

## 🔐 **Admin Features (Need Login)**

### **Step 1: Create Admin User**
```bash
python manage.py createsuperuser
```
- Username: `admin`
- Email: `admin@example.com`
- Password: `admin123`

### **Step 2: Login via Postman/curl**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Response will give you a TOKEN like:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {"username": "admin", "is_staff": true}
}
```

### **Step 3: Use Token for Admin Actions**
```bash
# Create new company (replace YOUR_TOKEN with actual token)
curl -X POST http://127.0.0.1:8000/api/companies/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "My New Company", "sector": "Technology"}'
```

---

## 📊 **Admin Dashboard Stats**

### **Get Dashboard Statistics**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://127.0.0.1:8000/api/auth/admin/stats/
```

**Sample Response:**
```json
{
  "overview": {
    "total_companies": 5,
    "total_ipos": 5,
    "total_users": 1,
    "total_issue_size": "8400.00"
  },
  "ipo_status": {
    "upcoming": 2,
    "open": 1,
    "listed": 2,
    "closed": 0
  }
}
```

### **Get Activity Logs**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://127.0.0.1:8000/api/auth/admin/logs/
```

---

## 📱 **Mobile App Integration**

### **Public API Calls (No Token Needed)**
```javascript
// Get all IPOs
fetch('http://127.0.0.1:8000/api/ipos/')
  .then(response => response.json())
  .then(data => console.log(data));

// Search IPOs
fetch('http://127.0.0.1:8000/api/ipos/search/?q=tech')
  .then(response => response.json())
  .then(data => console.log(data));
```

### **Admin API Calls (Token Required)**
```javascript
// Create IPO (admin only)
fetch('http://127.0.0.1:8000/api/ipos/', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    company: 1,
    issue_size: "1000.00",
    price_range_min: "100.00",
    price_range_max: "120.00",
    open_date: "2025-09-01",
    close_date: "2025-09-04",
    listing_date: "2025-09-10",
    status: "UPCOMING",
    lot_size: 100
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## 🛠️ **Using Postman (Recommended)**

### **Step 1: Import Collection**
- Open Postman
- Click "Import"
- Select `IPO_API_Collection.postman_collection.json`

### **Step 2: Test Endpoints**
- All public endpoints work immediately
- For admin endpoints, first run "Login" to get token
- Token is automatically saved for other requests

---

## 🔍 **Common API Responses**

### **IPO List Response:**
```json
[
  {
    "id": 1,
    "company_name": "Tech Innovations Pvt Ltd",
    "issue_size": "1500.00",
    "price_range": "₹120 - ₹140",
    "open_date": "2025-08-10",
    "close_date": "2025-08-13",
    "status": "UPCOMING",
    "is_featured": true,
    "days_to_open": 10
  }
]
```

### **Company Details Response:**
```json
{
  "id": 1,
  "name": "Tech Innovations Pvt Ltd",
  "description": "Leading technology company...",
  "sector": "Technology",
  "industry": "Software",
  "total_ipos": 1,
  "upcoming_ipos": 1
}
```

---

## ✅ **All Endpoints Work!**

Your API handles:
- ✅ Public access (no login needed)
- ✅ Admin access (JWT token required)
- ✅ File uploads (for PDF documents)
- ✅ Search and filtering
- ✅ Pagination for large datasets
- ✅ CORS for web/mobile apps

**Perfect for React frontend or mobile app development!** 📱

---

## 🆘 **Troubleshooting**

### **Server Not Running?**
```bash
python manage.py runserver
```

### **Database Error?**
```bash
python manage.py migrate
```

### **No Sample Data?**
```bash
python manage.py create_sample_data
```

### **Can't Login?**
```bash
python manage.py createsuperuser
```

---

**Your IPO Management API is ready for production use!** 🚀
