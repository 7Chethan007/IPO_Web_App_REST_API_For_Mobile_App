from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from companies.models import Company
from ipos.models import IPO
from datetime import date, timedelta
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Create sample data for IPO system'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before creating new data',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            IPO.objects.all().delete()
            Company.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing data cleared.'))

        self.stdout.write('Creating sample companies...')
        companies_data = [
            {
                'name': 'Tech Innovations Pvt Ltd',
                'description': 'Leading technology company specializing in AI and machine learning solutions.',
                'sector': 'Technology',
                'industry': 'Software',
                'website': 'https://techinnovations.com',
                'established_year': 2015,
                'headquarters': 'Bangalore, India'
            },
            {
                'name': 'Green Energy Solutions',
                'description': 'Renewable energy company focused on solar and wind power generation.',
                'sector': 'Energy',
                'industry': 'Renewable Energy',
                'website': 'https://greenenergy.com',
                'established_year': 2012,
                'headquarters': 'Mumbai, India'
            },
            {
                'name': 'HealthCare Plus',
                'description': 'Healthcare technology company providing telemedicine and digital health solutions.',
                'sector': 'Healthcare',
                'industry': 'Healthcare Technology',
                'website': 'https://healthcareplus.com',
                'established_year': 2018,
                'headquarters': 'Hyderabad, India'
            },
            {
                'name': 'FinTech Masters',
                'description': 'Financial technology company offering digital payment and banking solutions.',
                'sector': 'Financial Services',
                'industry': 'Fintech',
                'website': 'https://fintechmasters.com',
                'established_year': 2016,
                'headquarters': 'Gurgaon, India'
            },
            {
                'name': 'EduTech Solutions',
                'description': 'Educational technology platform providing online learning solutions.',
                'sector': 'Education',
                'industry': 'EdTech',
                'website': 'https://edutecsolutions.com',
                'established_year': 2017,
                'headquarters': 'Pune, India'
            }
        ]

        companies = []
        for company_data in companies_data:
            company, created = Company.objects.get_or_create(
                name=company_data['name'],
                defaults=company_data
            )
            companies.append(company)
            if created:
                self.stdout.write(f'Created company: {company.name}')

        self.stdout.write('Creating sample IPOs...')
        
        # Generate dates
        today = date.today()
        
        ipos_data = [
            {
                'company': companies[0],
                'issue_size': Decimal('1500.00'),
                'price_range_min': Decimal('120.00'),
                'price_range_max': Decimal('140.00'),
                'open_date': today + timedelta(days=10),
                'close_date': today + timedelta(days=13),
                'listing_date': today + timedelta(days=20),
                'board': 'MAIN',
                'status': 'UPCOMING',
                'lot_size': 100,
                'registrar': 'Link Intime India Pvt Ltd',
                'lead_managers': 'ICICI Securities, Kotak Mahindra Capital',
                'is_featured': True,
                'is_recommended': True
            },
            {
                'company': companies[1],
                'issue_size': Decimal('2500.00'),
                'price_range_min': Decimal('200.00'),
                'price_range_max': Decimal('250.00'),
                'open_date': today + timedelta(days=5),
                'close_date': today + timedelta(days=8),
                'listing_date': today + timedelta(days=15),
                'board': 'MAIN',
                'status': 'UPCOMING',
                'lot_size': 50,
                'registrar': 'Registrar to the Issue',
                'lead_managers': 'SBI Capital Markets, Axis Capital',
                'is_featured': True,
                'is_recommended': False
            },
            {
                'company': companies[2],
                'issue_size': Decimal('800.00'),
                'price_range_min': Decimal('80.00'),
                'price_range_max': Decimal('95.00'),
                'open_date': today + timedelta(days=1),
                'close_date': today + timedelta(days=3),
                'listing_date': today + timedelta(days=10),
                'board': 'SME',
                'status': 'OPEN',
                'lot_size': 150,
                'total_subscription': Decimal('2.5'),
                'retail_subscription': Decimal('1.8'),
                'qib_subscription': Decimal('3.2'),
                'nii_subscription': Decimal('2.1'),
                'registrar': 'Bigshare Services Pvt Ltd',
                'lead_managers': 'HDFC Bank, Yes Securities',
                'is_featured': False,
                'is_recommended': True
            },
            {
                'company': companies[3],
                'issue_size': Decimal('3000.00'),
                'price_range_min': Decimal('300.00'),
                'price_range_max': Decimal('350.00'),
                'listing_price': Decimal('385.00'),
                'open_date': today - timedelta(days=20),
                'close_date': today - timedelta(days=17),
                'listing_date': today - timedelta(days=10),
                'board': 'MAIN',
                'status': 'LISTED',
                'lot_size': 40,
                'total_subscription': Decimal('15.6'),
                'retail_subscription': Decimal('12.3'),
                'qib_subscription': Decimal('18.9'),
                'nii_subscription': Decimal('14.2'),
                'registrar': 'Karvy Fintech Pvt Ltd',
                'lead_managers': 'Morgan Stanley, Goldman Sachs',
                'listing_gains': Decimal('10.0'),
                'current_price': Decimal('420.50'),
                'is_featured': True,
                'is_recommended': True
            },
            {
                'company': companies[4],
                'issue_size': Decimal('600.00'),
                'price_range_min': Decimal('60.00'),
                'price_range_max': Decimal('75.00'),
                'listing_price': Decimal('72.00'),
                'open_date': today - timedelta(days=45),
                'close_date': today - timedelta(days=42),
                'listing_date': today - timedelta(days=35),
                'board': 'SME',
                'status': 'LISTED',
                'lot_size': 200,
                'total_subscription': Decimal('8.9'),
                'retail_subscription': Decimal('7.2'),
                'qib_subscription': Decimal('11.5'),
                'nii_subscription': Decimal('6.8'),
                'registrar': 'Cameo Corporate Services Ltd',
                'lead_managers': 'Edelweiss Financial Services',
                'listing_gains': Decimal('-4.0'),
                'current_price': Decimal('68.75'),
                'is_featured': False,
                'is_recommended': False
            }
        ]

        for ipo_data in ipos_data:
            ipo, created = IPO.objects.get_or_create(
                company=ipo_data['company'],
                open_date=ipo_data['open_date'],
                defaults=ipo_data
            )
            if created:
                self.stdout.write(f'Created IPO: {ipo.company.name} IPO')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(companies)} companies and {len(ipos_data)} IPOs'
            )
        )
