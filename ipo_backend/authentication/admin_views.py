from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from companies.models import Company
from ipos.models import IPO
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta


@api_view(['GET'])
@permission_classes([IsAdminUser])  # Keep this admin-only for security
def admin_users_list(request):
    """Get list of all users for admin"""
    try:
        users = User.objects.all()
        users_data = []
        
        for user in users:
            users_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'date_joined': user.date_joined.isoformat(),
                'last_login': user.last_login.isoformat() if user.last_login else None,
                'is_active': user.is_active
            })
        
        return Response({
            'users': users_data,
            'total_count': len(users_data)
        })
    except Exception as e:
        return Response({
            'error': f'Error fetching users: {str(e)}'
        }, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_stats(request):
    """Get dashboard statistics for authenticated users"""
    
    try:
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
    except Exception as e:
        print(f"Error in admin_stats: {str(e)}")
        return Response({
            'error': f'Internal server error: {str(e)}'
        }, status=500)


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
