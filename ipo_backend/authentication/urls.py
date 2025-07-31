from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, user_profile, register
from .admin_views import admin_stats, admin_logs

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    # Admin dashboard endpoints
    path('admin/stats/', admin_stats, name='admin_stats'),
    path('admin/logs/', admin_logs, name='admin_logs'),
]
