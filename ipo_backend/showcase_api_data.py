#!/usr/bin/env python
"""
Quick script to test API endpoints and showcase the populated data
"""
import os
import sys
import django
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipo_project.settings')
django.setup()

from companies.models import Company
from ipos.models import IPO, IPODocument, IPONews
from django.contrib.auth.models import User

def showcase_api_data():
    print("🚀 IPO API DATA SHOWCASE")
    print("=" * 50)

    # Show sample API-like queries
    print("📊 SAMPLE API QUERIES:")
    
    # 1. Get all IPOs with status filtering
    print("\n1. GET /api/ipos/?status=OPEN")
    open_ipos = IPO.objects.filter(status='OPEN')
    for ipo in open_ipos[:3]:
        print(f"   - {ipo.company.name}: ₹{ipo.price_range_min}-{ipo.price_range_max} ({ipo.open_date} to {ipo.close_date})")

    # 2. Get IPOs by board
    print("\n2. GET /api/ipos/?board=SME")
    sme_ipos = IPO.objects.filter(board='SME')[:3]
    for ipo in sme_ipos:
        print(f"   - {ipo.company.name}: ₹{ipo.issue_size} crores - {ipo.status}")

    # 3. Get companies by sector
    print("\n3. GET /api/companies/?sector=Healthcare")
    healthcare_companies = Company.objects.filter(sector='Healthcare')[:3]
    for company in healthcare_companies:
        ipo_count = company.ipos.count()
        print(f"   - {company.name} ({company.industry}) - {ipo_count} IPOs")

    # 4. Get featured IPOs
    print("\n4. GET /api/ipos/?is_featured=true")
    featured_ipos = IPO.objects.filter(is_featured=True)[:3]
    for ipo in featured_ipos:
        print(f"   - {ipo.company.name}: ₹{ipo.issue_size} crores - {ipo.status}")

    # 5. Get IPO documents
    print("\n5. GET /api/ipos/{id}/documents/")
    sample_ipo = IPO.objects.filter(documents__isnull=False).first()
    if sample_ipo:
        print(f"   IPO: {sample_ipo.company.name}")
        for doc in sample_ipo.documents.all()[:2]:
            print(f"     - {doc.document_type}: {doc.title}")

    # 6. Get IPO news
    print("\n6. GET /api/ipos/{id}/news/")
    sample_ipo_with_news = IPO.objects.filter(news__isnull=False).first()
    if sample_ipo_with_news:
        print(f"   IPO: {sample_ipo_with_news.company.name}")
        for news in sample_ipo_with_news.news.all()[:2]:
            print(f"     - {news.title}")

    # Statistics for dashboard
    print("\n📈 DASHBOARD STATISTICS:")
    print(f"   Total Companies: {Company.objects.count()}")
    print(f"   Total IPOs: {IPO.objects.count()}")
    print(f"   Open IPOs: {IPO.objects.filter(status='OPEN').count()}")
    print(f"   Upcoming IPOs: {IPO.objects.filter(status='UPCOMING').count()}")
    print(f"   Listed IPOs: {IPO.objects.filter(status='LISTED').count()}")
    print(f"   Featured IPOs: {IPO.objects.filter(is_featured=True).count()}")
    print(f"   Recommended IPOs: {IPO.objects.filter(is_recommended=True).count()}")

    # Market value statistics
    from django.db.models import Sum, Avg
    total_issue_value = IPO.objects.aggregate(Sum('issue_size'))['issue_size__sum'] or 0
    avg_issue_size = IPO.objects.aggregate(Avg('issue_size'))['issue_size__avg'] or 0
    
    print(f"\n💰 MARKET STATISTICS:")
    print(f"   Total Market Value: ₹{total_issue_value:,.0f} crores")
    print(f"   Average Issue Size: ₹{avg_issue_size:.0f} crores")

    print(f"\n✅ API DATA SHOWCASE COMPLETE!")

if __name__ == '__main__':
    showcase_api_data()
