from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from companies.models import Company
from ipos.models import IPO, IPODocument, IPONews
from decimal import Decimal
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate database with realistic IPO and company data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--companies',
            type=int,
            default=20,
            help='Number of companies to create (default: 20)'
        )
        parser.add_argument(
            '--ipos',
            type=int,
            default=30,
            help='Number of IPOs to create (default: 30)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before populating'
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            IPONews.objects.all().delete()
            IPODocument.objects.all().delete()
            IPO.objects.all().delete()
            Company.objects.all().delete()

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

        companies_count = options['companies']
        ipos_count = options['ipos']

        self.stdout.write(f'Creating {companies_count} companies...')
        companies = self.create_companies(companies_count, admin_user)
        
        self.stdout.write(f'Creating {ipos_count} IPOs...')
        ipos = self.create_ipos(ipos_count, companies, admin_user)
        
        self.stdout.write(f'Adding documents and news...')
        self.create_documents_and_news(ipos, admin_user)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(companies)} companies and {len(ipos)} IPOs'
            )
        )

    def create_companies(self, count, user):
        """Create realistic Indian companies"""
        company_data = [
            # Technology Companies
            {'name': 'TechCorp Solutions', 'sector': 'Information Technology', 'industry': 'Software Development', 'year': 2015},
            {'name': 'DataMind Technologies', 'sector': 'Information Technology', 'industry': 'Data Analytics', 'year': 2018},
            {'name': 'CloudNext Systems', 'sector': 'Information Technology', 'industry': 'Cloud Computing', 'year': 2017},
            {'name': 'FinTech Innovations', 'sector': 'Financial Services', 'industry': 'Financial Technology', 'year': 2019},
            {'name': 'AI Dynamics', 'sector': 'Information Technology', 'industry': 'Artificial Intelligence', 'year': 2020},
            
            # Healthcare & Pharma
            {'name': 'MediCare Pharmaceuticals', 'sector': 'Healthcare', 'industry': 'Pharmaceuticals', 'year': 2010},
            {'name': 'BioLife Sciences', 'sector': 'Healthcare', 'industry': 'Biotechnology', 'year': 2016},
            {'name': 'HealthTech Solutions', 'sector': 'Healthcare', 'industry': 'Medical Devices', 'year': 2018},
            {'name': 'GeneMed Research', 'sector': 'Healthcare', 'industry': 'Genetic Research', 'year': 2019},
            
            # Manufacturing & Industrial
            {'name': 'SteelCorp Industries', 'sector': 'Manufacturing', 'industry': 'Steel Production', 'year': 2005},
            {'name': 'AutoParts Manufacturing', 'sector': 'Automotive', 'industry': 'Auto Components', 'year': 2012},
            {'name': 'GreenEnergy Solutions', 'sector': 'Energy', 'industry': 'Renewable Energy', 'year': 2017},
            {'name': 'TextileCraft Ltd', 'sector': 'Textiles', 'industry': 'Textile Manufacturing', 'year': 2008},
            
            # Consumer & Retail
            {'name': 'FreshMart Retail', 'sector': 'Consumer Goods', 'industry': 'Retail', 'year': 2014},
            {'name': 'FoodCorp Limited', 'sector': 'FMCG', 'industry': 'Food Processing', 'year': 2011},
            {'name': 'StyleHub Fashion', 'sector': 'Consumer Goods', 'industry': 'Fashion & Apparel', 'year': 2016},
            
            # Real Estate & Construction
            {'name': 'UrbanBuild Developers', 'sector': 'Real Estate', 'industry': 'Real Estate Development', 'year': 2009},
            {'name': 'Infrastructure Corp', 'sector': 'Infrastructure', 'industry': 'Construction', 'year': 2007},
            
            # Financial Services
            {'name': 'MicroFinance Plus', 'sector': 'Financial Services', 'industry': 'Microfinance', 'year': 2013},
            {'name': 'InsureTech Solutions', 'sector': 'Financial Services', 'industry': 'Insurance Technology', 'year': 2020},
            
            # Telecommunications
            {'name': 'TeleConnect Networks', 'sector': 'Telecommunications', 'industry': 'Telecom Services', 'year': 2015},
            {'name': 'BroadBand Solutions', 'sector': 'Telecommunications', 'industry': 'Internet Services', 'year': 2018},
            
            # Education & Training
            {'name': 'EduTech Learning', 'sector': 'Education', 'industry': 'Educational Technology', 'year': 2019},
            {'name': 'SkillBridge Academy', 'sector': 'Education', 'industry': 'Skill Development', 'year': 2017},
            
            # Transportation & Logistics
            {'name': 'LogiMove Express', 'sector': 'Logistics', 'industry': 'Transportation', 'year': 2016},
            {'name': 'CargoFlow Systems', 'sector': 'Logistics', 'industry': 'Supply Chain', 'year': 2018},
        ]

        cities = ['Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad', 'Pune', 'Kolkata', 'Ahmedabad', 'Gurugram', 'Noida']
        
        companies = []
        existing_count = Company.objects.count()
        
        for i in range(min(count, len(company_data))):
            data = company_data[i]
            
            company, created = Company.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': f"{data['name']} is a leading company in the {data['industry']} sector, established in {data['year']}. The company focuses on providing innovative solutions and has established itself as a key player in the Indian market.",
                    'sector': data['sector'],
                    'industry': data['industry'],
                    'website': f"https://www.{data['name'].lower().replace(' ', '').replace('&', 'and')}.com",
                    'established_year': data['year'],
                    'headquarters': random.choice(cities),
                    'created_by': user,
                    'updated_by': user,
                }
            )
            
            if created:
                companies.append(company)
                self.stdout.write(f'  Created: {company.name}')
            else:
                companies.append(company)
                self.stdout.write(f'  Exists: {company.name}')

        return companies

    def create_ipos(self, count, companies, user):
        """Create IPOs with various statuses and realistic data"""
        ipos = []
        today = timezone.now().date()
        
        statuses = ['UPCOMING', 'OPEN', 'CLOSED', 'LISTED', 'WITHDRAWN']
        boards = ['MAIN', 'SME']
        
        # Ensure we have enough companies
        if len(companies) < count:
            self.stdout.write(self.style.WARNING(f'Only {len(companies)} companies available for {count} IPOs'))
        
        for i in range(count):
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
                listing_price = price_min + Decimal(str(random.randint(-50, 150)))  # Can be below or above issue price
                if listing_price < price_min:
                    listing_gains = Decimal(str(round(((listing_price - price_min) / price_min * 100), 2)))
                else:
                    listing_gains = Decimal(str(round(((listing_price - price_max) / price_max * 100), 2)))
                
                # Current price varies from listing price
                current_price = listing_price + Decimal(str(random.randint(-100, 200)))

            try:
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
                    created_by=user,
                    updated_by=user,
                )
                
                ipos.append(ipo)
                self.stdout.write(f'  Created IPO: {company.name} - {status} - ₹{issue_size} crores')
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating IPO for {company.name}: {e}'))

        return ipos

    def create_documents_and_news(self, ipos, user):
        """Create sample documents and news for IPOs"""
        doc_types = ['RHP', 'DRHP', 'PROSPECTUS', 'APPLICATION']
        
        for ipo in ipos[:10]:  # Add documents to first 10 IPOs
            # Add 1-2 documents per IPO
            for _ in range(random.randint(1, 2)):
                doc_type = random.choice(doc_types)
                IPODocument.objects.create(
                    ipo=ipo,
                    document_type=doc_type,
                    title=f"{ipo.company.name} {doc_type}",
                    description=f"Official {doc_type} document for {ipo.company.name} IPO",
                    uploaded_by=user
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
                IPONews.objects.create(
                    ipo=ipo,
                    title=title,
                    content=f"This is detailed news content about {title}. The company has shown strong fundamentals and market position in the {ipo.company.sector} sector.",
                    source="IPO News Network",
                    source_url="https://iponews.com",
                    created_by=user
                )
