# 🧪 Dummy Data Testing Guide - IPO Backend

This guide demonstrates how to effectively test your IPO backend using the populated dummy data.

## 🎯 Quick Testing Checklist

### ✅ Pre-Testing Setup
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Database populated (`python populate_ipo_data.py`)
- [ ] Data verified (`python verify_ipo_data.py`)
- [ ] Server running (`python manage.py runserver`)

## 🔍 Testing Scenarios

### 1. Admin Panel Testing

**Access**: http://localhost:8000/admin
**Credentials**: admin / admin123

**Test Cases**:
```bash
# Test admin login
✓ Login with admin credentials
✓ Navigate to Companies section
✓ Navigate to IPOs section
✓ Navigate to IPO Documents section
✓ Navigate to IPO News section

# Test data visibility
✓ View company list (should show 25+ companies)
✓ View IPO list (should show 30+ IPOs)
✓ Filter IPOs by status
✓ Filter IPOs by board type
✓ Search companies by name/sector
```

### 2. API Endpoint Testing

Use tools like Postman, curl, or Python requests:

```python
import requests

base_url = "http://localhost:8000/api"

# Test basic endpoints
def test_api_endpoints():
    # Test companies endpoint
    response = requests.get(f"{base_url}/companies/")
    print(f"Companies: {response.status_code} - {len(response.json())} records")
    
    # Test IPOs endpoint
    response = requests.get(f"{base_url}/ipos/")
    print(f"IPOs: {response.status_code} - {len(response.json())} records")
    
    # Test filtering
    response = requests.get(f"{base_url}/ipos/?status=OPEN")
    print(f"Open IPOs: {response.status_code} - {len(response.json())} records")
    
    response = requests.get(f"{base_url}/ipos/?board=SME")
    print(f"SME IPOs: {response.status_code} - {len(response.json())} records")

test_api_endpoints()
```

### 3. Database Query Testing

**Django Shell Testing**:
```python
# python manage.py shell

from companies.models import Company
from ipos.models import IPO
from django.utils import timezone

# Test basic queries
print(f"Total Companies: {Company.objects.count()}")
print(f"Total IPOs: {IPO.objects.count()}")

# Test filtering
healthcare_companies = Company.objects.filter(sector='Healthcare')
print(f"Healthcare Companies: {healthcare_companies.count()}")

# Test current market status
today = timezone.now().date()
open_ipos = IPO.objects.filter(
    status='OPEN',
    open_date__lte=today,
    close_date__gte=today
)
print(f"Currently Open IPOs: {open_ipos.count()}")
```

## 🎲 Sample Test Data

### Expected Data Counts
- **Companies**: 25+ records
- **IPOs**: 30+ records
- **Documents**: 20+ records
- **News**: 25+ records

### Sample IPOs by Status
```
OPEN (5 IPOs): Currently accepting applications
UPCOMING (8 IPOs): Opening in next 30-90 days
CLOSED (8 IPOs): Recently closed, awaiting listing
LISTED (4 IPOs): Successfully listed with gains data
WITHDRAWN (5 IPOs): Cancelled or withdrawn
```

## 🔬 Advanced Testing Scenarios

### 1. Performance Testing
```python
# Test large dataset queries
import time

start_time = time.time()
all_ipos = IPO.objects.select_related('company').all()
load_time = time.time() - start_time
print(f"Query execution time: {load_time:.3f} seconds")
```

### 2. Data Relationship Testing
```python
# Test foreign key relationships
for company in Company.objects.all()[:5]:
    ipo_count = company.ipos.count()
    print(f"{company.name}: {ipo_count} IPOs")
```

## 🎉 Testing Checklist Summary

### ✅ Basic Functionality
- [ ] Database populated successfully
- [ ] Admin panel accessible
- [ ] API endpoints responding
- [ ] Data integrity verified

### ✅ Data Quality
- [ ] All required fields populated
- [ ] Realistic data values
- [ ] Proper relationships maintained
- [ ] No data corruption

---

**Ready for Development!** Your IPO backend is thoroughly tested and ready for frontend integration! 🚀
