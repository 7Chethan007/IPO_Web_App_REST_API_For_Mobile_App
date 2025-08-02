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

from companies.models import Company
from ipos.models import IPO, IPODocument, IPONews
from django.contrib.auth.models import User
from django.db.models import Count, Q, F
from django.utils import timezone

def verify_data_integrity():
    print("🔍 VERIFYING DATA INTEGRITY AND RELATIONSHIPS")
    print("=" * 50)

    # Basic counts
    print(f"📊 DATABASE SUMMARY:")
    print(f"   👥 Users: {User.objects.count()}")
    print(f"   🏢 Companies: {Company.objects.count()}")
    print(f"   💼 IPOs: {IPO.objects.count()}")
    print(f"   📄 Documents: {IPODocument.objects.count()}")
    print(f"   📰 News Items: {IPONews.objects.count()}")

    # Check data quality
    print(f"\n🔍 DATA QUALITY CHECKS:")
    
    # Check for companies without IPOs
    companies_without_ipos = Company.objects.annotate(
        ipo_count=Count('ipos')
    ).filter(ipo_count=0)
    
    print(f"   Companies without IPOs: {companies_without_ipos.count()}")
    if companies_without_ipos.count() > 0:
        for company in companies_without_ipos[:3]:
            print(f"     - {company.name}")

    # Check for IPOs with invalid dates
    invalid_date_ipos = IPO.objects.filter(
        Q(open_date__gte=F('close_date')) |
        Q(close_date__gte=F('listing_date'))
    )
    
    if invalid_date_ipos.exists():
        print(f"   ❌ IPOs with invalid dates: {invalid_date_ipos.count()}")
    else:
        print(f"   ✅ All IPO dates are valid")

    # Check subscription data
    invalid_subscription = IPO.objects.filter(total_subscription__lt=0)
    if invalid_subscription.exists():
        print(f"   ❌ IPOs with invalid subscription: {invalid_subscription.count()}")
    else:
        print(f"   ✅ All subscription data is valid")

    # Check price ranges
    invalid_prices = IPO.objects.filter(price_range_min__gte=F('price_range_max'))
    if invalid_prices.exists():
        print(f"   ❌ IPOs with invalid price ranges: {invalid_prices.count()}")
    else:
        print(f"   ✅ All price ranges are valid")

    # IPO Status Distribution
    print(f"\n📈 IPO STATUS BREAKDOWN:")
    total_ipos = IPO.objects.count()
    for status_code, status_name in IPO.STATUS_CHOICES:
        count = IPO.objects.filter(status=status_code).count()
        percentage = (count / total_ipos * 100) if total_ipos > 0 else 0
        print(f"   {status_name}: {count} ({percentage:.1f}%)")

    # Board Distribution
    print(f"\n🎯 BOARD DISTRIBUTION:")
    main_board = IPO.objects.filter(board='MAIN').count()
    sme_board = IPO.objects.filter(board='SME').count()
    if total_ipos > 0:
        print(f"   Main Board: {main_board} ({main_board/total_ipos*100:.1f}%)")
        print(f"   SME Board: {sme_board} ({sme_board/total_ipos*100:.1f}%)")

    # Sector Analysis
    print(f"\n🏭 SECTOR ANALYSIS:")
    sectors = Company.objects.values('sector').annotate(
        company_count=Count('id'),
        ipo_count=Count('ipos')
    ).order_by('-ipo_count')
    
    for sector_data in sectors:
        sector = sector_data['sector']
        company_count = sector_data['company_count']
        ipo_count = sector_data['ipo_count']
        if sector:
            print(f"   {sector}: {company_count} companies, {ipo_count} IPOs")

    # Recent IPOs
    print(f"\n🕒 RECENT IPOs (Last 5):")
    recent_ipos = IPO.objects.order_by('-created_at')[:5]
    for ipo in recent_ipos:
        print(f"   {ipo.company.name} - {ipo.status} - ₹{ipo.issue_size} crores ({ipo.board} Board)")

    # Featured and Recommended
    featured = IPO.objects.filter(is_featured=True).count()
    recommended = IPO.objects.filter(is_recommended=True).count()
    print(f"\n⭐ SPECIAL CATEGORIES:")
    print(f"   Featured IPOs: {featured}")
    print(f"   Recommended IPOs: {recommended}")

    # Current Market Status
    today = timezone.now().date()
    print(f"\n📅 CURRENT MARKET STATUS (as of {today}):")
    
    # IPOs currently open
    open_ipos = IPO.objects.filter(
        status='OPEN',
        open_date__lte=today,
        close_date__gte=today
    )
    print(f"   Currently Open IPOs: {open_ipos.count()}")
    for ipo in open_ipos:
        days_left = (ipo.close_date - today).days
        print(f"     - {ipo.company.name}: {days_left} days left")
    
    # IPOs opening soon
    upcoming_ipos = IPO.objects.filter(
        status='UPCOMING',
        open_date__gt=today,
        open_date__lte=today + timezone.timedelta(days=30)
    ).order_by('open_date')
    
    print(f"   Opening in Next 30 Days: {upcoming_ipos.count()}")
    for ipo in upcoming_ipos[:3]:
        days_to_open = (ipo.open_date - today).days
        print(f"     - {ipo.company.name}: Opens in {days_to_open} days")

    # Issue Size Analysis
    print(f"\n💰 ISSUE SIZE ANALYSIS:")
    large_ipos = IPO.objects.filter(issue_size__gte=1000).count()
    medium_ipos = IPO.objects.filter(issue_size__gte=100, issue_size__lt=1000).count()
    small_ipos = IPO.objects.filter(issue_size__lt=100).count()
    
    print(f"   Large IPOs (≥₹1000 cr): {large_ipos}")
    print(f"   Medium IPOs (₹100-999 cr): {medium_ipos}")
    print(f"   Small IPOs (<₹100 cr): {small_ipos}")

    # Top companies by market cap (using issue size as proxy)
    print(f"\n🏆 TOP 5 LARGEST IPOs:")
    top_ipos = IPO.objects.order_by('-issue_size')[:5]
    for i, ipo in enumerate(top_ipos, 1):
        print(f"   {i}. {ipo.company.name}: ₹{ipo.issue_size} crores ({ipo.status})")

    print(f"\n✅ DATA INTEGRITY VERIFICATION COMPLETE!")
    print("=" * 50)

if __name__ == '__main__':
    verify_data_integrity()
