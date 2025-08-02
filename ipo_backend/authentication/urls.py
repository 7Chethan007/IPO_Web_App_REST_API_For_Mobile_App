from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, user_profile, register
from .admin_views import admin_stats, admin_logs, admin_users_list

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin/', CustomTokenObtainPairView.as_view(), name='signin'),  # Add alias for signin
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('signup/', register, name='signup'),  # Add alias for signup
    path('profile/', user_profile, name='user_profile'),
    # Admin dashboard endpoints
    path('admin/stats/', admin_stats, name='admin_stats'),
    path('admin/logs/', admin_logs, name='admin_logs'),
    path('admin/users/', admin_users_list, name='admin_users_list'),
]