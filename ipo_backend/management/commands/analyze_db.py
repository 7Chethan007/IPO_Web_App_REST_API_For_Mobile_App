from django.core.management.base import BaseCommand
from django.db import connection
from companies.models import Company
from ipos.models import IPO, IPODocument, IPONews
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Analyze current database structure and data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== DATABASE ANALYSIS ===\n'))

        # Get database info
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
        
        self.stdout.write(f'Database Tables: {len(tables)}')
        for table in tables:
            self.stdout.write(f'  - {table[0]}')

        # Analyze data counts
        self.stdout.write(f'\n=== DATA COUNTS ===')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Companies: {Company.objects.count()}')
        self.stdout.write(f'IPOs: {IPO.objects.count()}')
        self.stdout.write(f'IPO Documents: {IPODocument.objects.count()}')
        self.stdout.write(f'IPO News: {IPONews.objects.count()}')

        # Analyze companies
        if Company.objects.exists():
            self.stdout.write(f'\n=== EXISTING COMPANIES ===')
            for company in Company.objects.all()[:10]:
                ipo_count = company.ipos.count()
                self.stdout.write(f'  {company.name} ({company.sector}) - {ipo_count} IPOs')

        # Analyze IPOs by status
        if IPO.objects.exists():
            self.stdout.write(f'\n=== IPO STATUS BREAKDOWN ===')
            for status_code, status_name in IPO.STATUS_CHOICES:
                count = IPO.objects.filter(status=status_code).count()
                self.stdout.write(f'  {status_name}: {count}')

        # Analyze IPOs by board
        if IPO.objects.exists():
            self.stdout.write(f'\n=== IPO BOARD BREAKDOWN ===')
            for board_code, board_name in IPO.BOARD_CHOICES:
                count = IPO.objects.filter(board=board_code).count()
                self.stdout.write(f'  {board_name}: {count}')

        # Analyze sectors
        sectors = Company.objects.values_list('sector', flat=True).distinct()
        self.stdout.write(f'\n=== SECTORS ({len(sectors)}) ===')
        for sector in sectors:
            if sector:
                count = Company.objects.filter(sector=sector).count()
                self.stdout.write(f'  {sector}: {count} companies')

        # Recent IPOs
        recent_ipos = IPO.objects.order_by('-created_at')[:5]
        if recent_ipos:
            self.stdout.write(f'\n=== RECENT IPOs ===')
            for ipo in recent_ipos:
                self.stdout.write(f'  {ipo.company.name} - {ipo.status} - ₹{ipo.issue_size} crores')

        self.stdout.write(self.style.SUCCESS('\n=== ANALYSIS COMPLETE ==='))
