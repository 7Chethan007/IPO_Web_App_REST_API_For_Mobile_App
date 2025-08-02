from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from companies.models import Company


class IPO(models.Model):
    """
    IPO (Initial Public Offering) model to store all IPO related information.
    Simplified structure for easy understanding and maintenance.
    """
    BOARD_CHOICES = [
        ('MAIN', 'Main Board'),
        ('SME', 'SME Board'),
    ]
    
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('LISTED', 'Listed'),
        ('WITHDRAWN', 'Withdrawn'),
    ]
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='ipos')
    issue_size = models.DecimalField(max_digits=15, decimal_places=2, help_text="Issue size in crores")
    price_range_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_range_max = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Important Dates
    open_date = models.DateField(help_text="IPO opening date")
    close_date = models.DateField(help_text="IPO closing date")
    listing_date = models.DateField(help_text="Expected listing date")
    
    # IPO Details
    board = models.CharField(max_length=10, choices=BOARD_CHOICES, default='MAIN')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UPCOMING')
    lot_size = models.IntegerField(help_text="Minimum lot size")
    
    # Subscription Information (how many times IPO was subscribed)
    total_subscription = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0,
        help_text="Total subscription in times (e.g., 2.5 means 2.5x subscribed)"
    )
    retail_subscription = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0,
        help_text="Retail investor subscription in times"
    )
    institutional_subscription = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0,
        help_text="Institutional investor subscription in times"
    )
    
    # Documents
    rhp_document = models.FileField(upload_to='documents/rhps/', blank=True, null=True, help_text="Red Herring Prospectus")
    drhp_document = models.FileField(upload_to='documents/drhps/', blank=True, null=True, help_text="Draft Red Herring Prospectus")
    
    # Additional Information
    registrar = models.CharField(max_length=255, blank=True, null=True, help_text="Registrar to the issue")
    lead_managers = models.TextField(blank=True, null=True, help_text="Lead managers (comma separated)")
    
    # Performance after listing
    listing_gains = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Listing gains in percentage")
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Current market price")
    
    # Featured/Recommended
    is_featured = models.BooleanField(default=False, help_text="Mark as featured IPO")
    is_recommended = models.BooleanField(default=False, help_text="Mark as recommended IPO")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_ipos')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_ipos')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "IPO"
        verbose_name_plural = "IPOs"

    def __str__(self):
        return f"{self.company.name} IPO - {self.status}"

    @property
    def is_open(self):
        """Check if IPO is currently open for subscription"""
        today = timezone.now().date()
        return self.open_date <= today <= self.close_date

    @property
    def days_to_open(self):
        """Get number of days until IPO opens"""
        today = timezone.now().date()
        if self.open_date > today:
            return (self.open_date - today).days
        return 0

    @property
    def days_to_close(self):
        """Get number of days until IPO closes"""
        today = timezone.now().date()
        if self.close_date > today:
            return (self.close_date - today).days
        return 0

    @property
    def price_range(self):
        """Get formatted price range"""
        return f"₹{self.price_range_min} - ₹{self.price_range_max}"

    @property
    def total_issue_value(self):
        """Get formatted issue size"""
        return f"₹{self.issue_size} crores"

    @property
    def is_subscribed(self):
        """Check if IPO is oversubscribed"""
        return self.total_subscription > 1.0

    def clean(self):
        """Validate the IPO data before saving"""
        if self.price_range_min >= self.price_range_max:
            raise ValidationError("Minimum price must be less than maximum price")
        if self.open_date >= self.close_date:
            raise ValidationError("Open date must be before close date")
        if self.close_date >= self.listing_date:
            raise ValidationError("Close date must be before listing date")


class IPODocument(models.Model):
    """
    Store documents related to IPO (prospectus, application forms, etc.)
    """
    DOCUMENT_TYPES = [
        ('RHP', 'Red Herring Prospectus'),
        ('DRHP', 'Draft Red Herring Prospectus'),
        ('PROSPECTUS', 'Prospectus'),
        ('APPLICATION', 'Application Form'),
        ('OTHER', 'Other'),
    ]
    
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='ipo_documents/')
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.ipo.company.name} - {self.title}"


class IPONews(models.Model):
    """
    Store news articles and updates related to IPOs
    """
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=255)
    content = models.TextField()
    source = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "IPO News"

    def __str__(self):
        return f"{self.ipo.company.name} - {self.title}"
