#!/usr/bin/env python
import os
import sys
import django
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipo_project.settings')
django.setup()

from django.contrib.auth.models import User
from companies.models import Company
from ipos.models import IPO, IPODocument, IPONews
from decimal import Decimal
import random
from datetime import date, timedelta
from django.utils import timezone

def create_realistic_data():
    print("🚀 Starting IPO Database Population...")
    
    # Create admin user if doesn't exist
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@ipo.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("✅ Created admin user (username: admin, password: admin123)")

    # Company data with realistic Indian companies
    company_data = [
        # Technology Companies
        {'name': 'TechCorp Solutions', 'sector': 'Information Technology', 'industry': 'Software Development', 'year': 2015, 'city': 'Bangalore'},
        {'name': 'DataMind Technologies', 'sector': 'Information Technology', 'industry': 'Data Analytics', 'year': 2018, 'city': 'Hyderabad'},
        {'name': 'CloudNext Systems', 'sector': 'Information Technology', 'industry': 'Cloud Computing', 'year': 2017, 'city': 'Pune'},
        {'name': 'FinTech Innovations', 'sector': 'Financial Services', 'industry': 'Financial Technology', 'year': 2019, 'city': 'Mumbai'},
        {'name': 'AI Dynamics', 'sector': 'Information Technology', 'industry': 'Artificial Intelligence', 'year': 2020, 'city': 'Chennai'},
        
        # Healthcare & Pharma
        {'name': 'MediCare Pharmaceuticals', 'sector': 'Healthcare', 'industry': 'Pharmaceuticals', 'year': 2010, 'city': 'Mumbai'},
        {'name': 'BioLife Sciences', 'sector': 'Healthcare', 'industry': 'Biotechnology', 'year': 2016, 'city': 'Bangalore'},
        {'name': 'HealthTech Solutions', 'sector': 'Healthcare', 'industry': 'Medical Devices', 'year': 2018, 'city': 'Delhi'},
        {'name': 'GeneMed Research', 'sector': 'Healthcare', 'industry': 'Genetic Research', 'year': 2019, 'city': 'Hyderabad'},
        
        # Manufacturing & Industrial
        {'name': 'SteelCorp Industries', 'sector': 'Manufacturing', 'industry': 'Steel Production', 'year': 2005, 'city': 'Kolkata'},
        {'name': 'AutoParts Manufacturing', 'sector': 'Automotive', 'industry': 'Auto Components', 'year': 2012, 'city': 'Chennai'},
        {'name': 'GreenEnergy Solutions', 'sector': 'Energy', 'industry': 'Renewable Energy', 'year': 2017, 'city': 'Ahmedabad'},
        {'name': 'TextileCraft Ltd', 'sector': 'Textiles', 'industry': 'Textile Manufacturing', 'year': 2008, 'city': 'Mumbai'},
        
        # Consumer & Retail
        {'name': 'FreshMart Retail', 'sector': 'Consumer Goods', 'industry': 'Retail', 'year': 2014, 'city': 'Delhi'},
        {'name': 'FoodCorp Limited', 'sector': 'FMCG', 'industry': 'Food Processing', 'year': 2011, 'city': 'Mumbai'},
        {'name': 'StyleHub Fashion', 'sector': 'Consumer Goods', 'industry': 'Fashion & Apparel', 'year': 2016, 'city': 'Bangalore'},
        
        # Real Estate & Construction
        {'name': 'UrbanBuild Developers', 'sector': 'Real Estate', 'industry': 'Real Estate Development', 'year': 2009, 'city': 'Gurugram'},
        {'name': 'Infrastructure Corp', 'sector': 'Infrastructure', 'industry': 'Construction', 'year': 2007, 'city': 'Mumbai'},
        
        # Financial Services
        {'name': 'MicroFinance Plus', 'sector': 'Financial Services', 'industry': 'Microfinance', 'year': 2013, 'city': 'Chennai'},
        {'name': 'InsureTech Solutions', 'sector': 'Financial Services', 'industry': 'Insurance Technology', 'year': 2020, 'city': 'Pune'},
    ]

    print(f"📊 Creating {len(company_data)} companies...")
    companies = []
    
    for data in company_data:
        company, created = Company.objects.get_or_create(
            name=data['name'],
            defaults={
                'description': f"{data['name']} is a leading company in the {data['industry']} sector, established in {data['year']}. The company focuses on providing innovative solutions and has established itself as a key player in the Indian market.",
                'sector': data['sector'],
                'industry': data['industry'],
                'website': f"https://www.{data['name'].lower().replace(' ', '').replace('&', 'and')}.com",
                'established_year': data['year'],
                'headquarters': data['city'],
                'created_by': admin_user,
                'updated_by': admin_user,
            }
        )
        companies.append(company)
        status = "✅ Created" if created else "🔄 Exists"
        print(f"  {status}: {company.name} ({company.sector})")

    print(f"\n💼 Creating 30+ IPOs with various statuses...")
    
    # IPO generation
    statuses = ['UPCOMING', 'OPEN', 'CLOSED', 'LISTED', 'WITHDRAWN']
    boards = ['MAIN', 'SME']
    today = timezone.now().date()
    
    ipo_count = 0
    target_ipos = 35
    
    # Create multiple IPOs for some companies
    for i in range(target_ipos):
        company = random.choice(companies)
        status = random.choice(statuses)
        board = random.choice(boards)
        
        # Generate realistic dates based on status
        if status == 'UPCOMING':
            open_date = today + timedelta(days=random.randint(5, 90))
            close_date = open_date + timedelta(days=random.randint(3, 7))
            listing_date = close_date + timedelta(days=random.randint(5, 15))
        elif status == 'OPEN':
            open_date = today - timedelta(days=random.randint(0, 3))
            close_date = today + timedelta(days=random.randint(1, 5))
            listing_date = close_date + timedelta(days=random.randint(5, 15))
        elif status == 'CLOSED':
            open_date = today - timedelta(days=random.randint(10, 30))
            close_date = today - timedelta(days=random.randint(1, 8))
            listing_date = close_date + timedelta(days=random.randint(5, 15))
        elif status == 'LISTED':
            open_date = today - timedelta(days=random.randint(30, 180))
            close_date = open_date + timedelta(days=random.randint(3, 7))
            listing_date = close_date + timedelta(days=random.randint(5, 15))
        else:  # WITHDRAWN
            open_date = today - timedelta(days=random.randint(5, 30))
            close_date = open_date + timedelta(days=random.randint(3, 7))
            listing_date = close_date + timedelta(days=random.randint(5, 15))

        # Generate realistic financial data
        if board == 'SME':
            issue_size = Decimal(str(random.randint(5, 100)))  # 5-100 crores for SME
            price_min = Decimal(str(random.randint(50, 200)))
        else:
            issue_size = Decimal(str(random.randint(100, 5000)))  # 100-5000 crores for Main Board
            price_min = Decimal(str(random.randint(100, 500)))
        
        price_max = price_min + Decimal(str(random.randint(10, 100)))
        lot_size = random.choice([10, 15, 20, 25, 50, 100])
        
        # Generate subscription data
        total_sub = Decimal(str(round(random.uniform(0.5, 50.0), 2)))
        retail_sub = Decimal(str(round(random.uniform(0.3, 30.0), 2)))
        institutional_sub = Decimal(str(round(random.uniform(0.2, 25.0), 2)))
        
        # Generate listing price and gains for listed IPOs
        listing_price = None
        listing_gains = None
        current_price = None
        
        if status == 'LISTED':
            listing_price = price_min + Decimal(str(random.randint(-50, 150)))
            if listing_price < price_min:
                listing_gains = Decimal(str(round(((listing_price - price_min) / price_min * 100), 2)))
            else:
                listing_gains = Decimal(str(round(((listing_price - price_max) / price_max * 100), 2)))
            current_price = listing_price + Decimal(str(random.randint(-100, 200)))

        try:
            # Check if IPO already exists for this company
            existing_ipo = IPO.objects.filter(company=company).first()
            if existing_ipo and random.random() < 0.7:  # 70% chance to skip if company already has IPO
                continue
                
            ipo = IPO.objects.create(
                company=company,
                issue_size=issue_size,
                price_range_min=price_min,
                price_range_max=price_max,
                listing_price=listing_price,
                open_date=open_date,
                close_date=close_date,
                listing_date=listing_date,
                board=board,
                status=status,
                lot_size=lot_size,
                total_subscription=total_sub,
                retail_subscription=retail_sub,
                institutional_subscription=institutional_sub,
                registrar=random.choice([
                    'Link Intime India Pvt Ltd',
                    'KFin Technologies Ltd',
                    'Registrar and Transfer Agents',
                    'Bigshare Services Pvt Ltd',
                    'Skyline Financial Services'
                ]),
                lead_managers=random.choice([
                    'ICICI Securities, Kotak Mahindra Capital',
                    'Morgan Stanley, Goldman Sachs',
                    'JM Financial, Axis Capital',
                    'SBI Capital Markets, HDFC Bank',
                    'YES Securities, IIFL Securities'
                ]),
                listing_gains=listing_gains,
                current_price=current_price,
                is_featured=random.choice([True, False]),
                is_recommended=random.choice([True, False]),
                created_by=admin_user,
                updated_by=admin_user,
            )
            
            ipo_count += 1
            print(f"  ✅ Created: {company.name} IPO - {status} - {board} Board - ₹{issue_size} crores")
            
        except Exception as e:
            print(f"  ❌ Error creating IPO for {company.name}: {e}")

    # Add some documents and news
    print(f"\n📄 Adding documents and news...")
    ipos = IPO.objects.all()[:15]  # First 15 IPOs
    doc_types = ['RHP', 'DRHP', 'PROSPECTUS', 'APPLICATION']
    
    for ipo in ipos:
        # Add 1-2 documents per IPO
        for _ in range(random.randint(1, 2)):
            doc_type = random.choice(doc_types)
            IPODocument.objects.get_or_create(
                ipo=ipo,
                document_type=doc_type,
                title=f"{ipo.company.name} {doc_type}",
                defaults={
                    'description': f"Official {doc_type} document for {ipo.company.name} IPO",
                    'uploaded_by': admin_user
                }
            )

        # Add 1-3 news items per IPO
        news_templates = [
            f"{ipo.company.name} announces IPO pricing and timeline",
            f"Market analysts bullish on {ipo.company.name} IPO prospects",
            f"{ipo.company.name} IPO sees strong institutional interest",
            f"Retail investors show keen interest in {ipo.company.name}",
            f"{ipo.company.name} IPO subscription details released"
        ]
        
        for _ in range(random.randint(1, 3)):
            title = random.choice(news_templates)
            IPONews.objects.get_or_create(
                ipo=ipo,
                title=title,
                defaults={
                    'content': f"This is detailed news content about {title}. The company has shown strong fundamentals and market position in the {ipo.company.sector} sector.",
                    'source': "IPO News Network",
                    'source_url': "https://iponews.com",
                    'created_by': admin_user
                }
            )

    # Final summary
    print(f"\n🎉 DATA POPULATION COMPLETE!")
    print(f"📈 Summary:")
    print(f"   Companies: {Company.objects.count()}")
    print(f"   IPOs: {IPO.objects.count()}")
    print(f"   Documents: {IPODocument.objects.count()}")
    print(f"   News Items: {IPONews.objects.count()}")
    
    # Status breakdown
    print(f"\n📊 IPO Status Breakdown:")
    for status_code, status_name in IPO.STATUS_CHOICES:
        count = IPO.objects.filter(status=status_code).count()
        print(f"   {status_name}: {count}")
    
    # Board breakdown
    print(f"\n🏢 Board Breakdown:")
    main_board = IPO.objects.filter(board='MAIN').count()
    sme_board = IPO.objects.filter(board='SME').count()
    print(f"   Main Board: {main_board}")
    print(f"   SME Board: {sme_board}")
    
    # Sector breakdown
    print(f"\n🏭 Sector Breakdown:")
    sectors = Company.objects.values_list('sector', flat=True).distinct()
    for sector in sectors:
        if sector:
            count = Company.objects.filter(sector=sector).count()
            ipo_count = IPO.objects.filter(company__sector=sector).count()
            print(f"   {sector}: {count} companies, {ipo_count} IPOs")

if __name__ == '__main__':
    create_realistic_data()
