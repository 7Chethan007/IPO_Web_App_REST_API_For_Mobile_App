from django.core.management.base import BaseCommand
from companies.models import Company
from ipos.models import IPO, IPODocument, IPONews
from django.db.models import Count, Q, F
from django.utils import timezone

class Command(BaseCommand):
    help = 'Verify data integrity and relationships'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== DATA INTEGRITY VERIFICATION ===\n'))

        # Check for companies without IPOs
        companies_without_ipos = Company.objects.annotate(
            ipo_count=Count('ipos')
        ).filter(ipo_count=0)
        
        self.stdout.write(f'Companies without IPOs: {companies_without_ipos.count()}')
        for company in companies_without_ipos[:5]:
            self.stdout.write(f'  - {company.name}')

        # Check for IPOs with invalid dates
        today = timezone.now().date()
        invalid_date_ipos = IPO.objects.filter(
            Q(open_date__gte=F('close_date')) |
            Q(close_date__gte=F('listing_date'))
        )
        
        if invalid_date_ipos.exists():
            self.stdout.write(self.style.ERROR(f'\nIPOs with invalid dates: {invalid_date_ipos.count()}'))
        else:
            self.stdout.write(self.style.SUCCESS('\n✓ All IPO dates are valid'))

        # Check subscription data
        invalid_subscription = IPO.objects.filter(
            total_subscription__lt=0
        )
        
        if invalid_subscription.exists():
            self.stdout.write(self.style.ERROR(f'IPOs with invalid subscription: {invalid_subscription.count()}'))
        else:
            self.stdout.write(self.style.SUCCESS('✓ All subscription data is valid'))

        # Check price ranges
        invalid_prices = IPO.objects.filter(
            price_range_min__gte=F('price_range_max')
        )
        
        if invalid_prices.exists():
            self.stdout.write(self.style.ERROR(f'IPOs with invalid price ranges: {invalid_prices.count()}'))
        else:
            self.stdout.write(self.style.SUCCESS('✓ All price ranges are valid'))

        # Check for orphaned documents
        orphaned_docs = IPODocument.objects.filter(ipo__isnull=True).count()
        orphaned_news = IPONews.objects.filter(ipo__isnull=True).count()
        
        self.stdout.write(f'\nOrphaned documents: {orphaned_docs}')
        self.stdout.write(f'Orphaned news: {orphaned_news}')

        # Summary statistics
        self.stdout.write(f'\n=== SUMMARY STATISTICS ===')
        
        # IPO status distribution
        for status_code, status_name in IPO.STATUS_CHOICES:
            count = IPO.objects.filter(status=status_code).count()
            percentage = (count / IPO.objects.count() * 100) if IPO.objects.count() > 0 else 0
            self.stdout.write(f'{status_name}: {count} ({percentage:.1f}%)')

        # Board distribution
        main_board = IPO.objects.filter(board='MAIN').count()
        sme_board = IPO.objects.filter(board='SME').count()
        total_ipos = IPO.objects.count()
        
        if total_ipos > 0:
            self.stdout.write(f'\nMain Board: {main_board} ({main_board/total_ipos*100:.1f}%)')
            self.stdout.write(f'SME Board: {sme_board} ({sme_board/total_ipos*100:.1f}%)')

        # Featured and recommended
        featured = IPO.objects.filter(is_featured=True).count()
        recommended = IPO.objects.filter(is_recommended=True).count()
        
        self.stdout.write(f'\nFeatured IPOs: {featured}')
        self.stdout.write(f'Recommended IPOs: {recommended}')

        self.stdout.write(self.style.SUCCESS('\n=== VERIFICATION COMPLETE ==='))
