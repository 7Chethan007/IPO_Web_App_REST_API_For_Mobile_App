from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from companies.models import Company
from ipos.models import IPO
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_stats(request):
    """Get dashboard statistics for admin"""
    
    # Basic counts
    total_companies = Company.objects.count()
    total_ipos = IPO.objects.count()
    total_users = User.objects.count()
    
    # IPO status breakdown
    upcoming_ipos = IPO.objects.filter(open_date__gt=timezone.now().date()).count()
    open_ipos = IPO.objects.filter(
        open_date__lte=timezone.now().date(),
        close_date__gte=timezone.now().date()
    ).count()
    listed_ipos = IPO.objects.filter(status='LISTED').count()
    
    # Recent activity (last 7 days)
    week_ago = timezone.now() - timedelta(days=7)
    recent_companies = Company.objects.filter(created_at__gte=week_ago).count()
    recent_ipos = IPO.objects.filter(created_at__gte=week_ago).count()
    
    # Financial stats
    total_issue_size = IPO.objects.aggregate(
        total=Sum('issue_size')
    )['total'] or 0
    
    return Response({
        'overview': {
            'total_companies': total_companies,
            'total_ipos': total_ipos,
            'total_users': total_users,
            'total_issue_size': str(total_issue_size)
        },
        'ipo_status': {
            'upcoming': upcoming_ipos,
            'open': open_ipos,
            'listed': listed_ipos,
            'closed': total_ipos - upcoming_ipos - open_ipos - listed_ipos
        },
        'recent_activity': {
            'companies_added': recent_companies,
            'ipos_added': recent_ipos
        }
    })


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_logs(request):
    """Get recent admin activities"""
    
    # Get recent companies and IPOs with creator info
    recent_companies = Company.objects.select_related('created_by').order_by('-created_at')[:10]
    recent_ipos = IPO.objects.select_related('created_by', 'company').order_by('-created_at')[:10]
    
    activities = []
    
    # Add company activities
    for company in recent_companies:
        activities.append({
            'type': 'company_created',
            'message': f'Company "{company.name}" was created',
            'user': company.created_by.username if company.created_by else 'System',
            'timestamp': company.created_at,
            'object_id': company.id
        })
    
    # Add IPO activities
    for ipo in recent_ipos:
        activities.append({
            'type': 'ipo_created',
            'message': f'IPO for "{ipo.company.name}" was created',
            'user': ipo.created_by.username if ipo.created_by else 'System',
            'timestamp': ipo.created_at,
            'object_id': ipo.id
        })
    
    # Sort by timestamp
    activities.sort(key=lambda x: x['timestamp'], reverse=True)
    
    return Response({
        'activities': activities[:20]  # Return latest 20 activities
    })
