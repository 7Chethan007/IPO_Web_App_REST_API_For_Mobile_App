#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipo_project.settings')
django.setup()

from django.contrib.auth.models import User

def check_and_update_superuser():
    print("=== CHECKING SUPERUSERS ===")
    
    # Check for existing superuser "chethan"
    try:
        chethan = User.objects.get(username='chethan')
        print(f"Found user 'chethan':")
        print(f"  - Email: {chethan.email}")
        print(f"  - Is staff: {chethan.is_staff}")
        print(f"  - Is superuser: {chethan.is_superuser}")
        
        # Add email if missing
        if not chethan.email:
            chethan.email = 'chethan@admin.com'
            chethan.save()
            print(f"  - Added email: {chethan.email}")
        
        # Make sure user is superuser and staff
        if not chethan.is_superuser:
            chethan.is_superuser = True
            chethan.save()
            print("  - Made user superuser")
            
        if not chethan.is_staff:
            chethan.is_staff = True
            chethan.save()
            print("  - Made user staff")
            
        print("\n=== SUPERUSER READY ===")
        print(f"Username: {chethan.username}")
        print(f"Email: {chethan.email}")
        print(f"Password: Chethan@007 (from .env)")
        
    except User.DoesNotExist:
        print("User 'chethan' not found. Creating new superuser...")
        
        # Create superuser
        chethan = User.objects.create_superuser(
            username='chethan',
            email='chethan@admin.com',
            password='Chethan@007'
        )
        print(f"Created superuser:")
        print(f"  - Username: {chethan.username}")
        print(f"  - Email: {chethan.email}")
        print(f"  - Password: Chethan@007")
    
    print("\n=== ALL SUPERUSERS ===")
    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        print(f"- {user.username} ({user.email}) - Staff: {user.is_staff}")

if __name__ == '__main__':
    check_and_update_superuser()
