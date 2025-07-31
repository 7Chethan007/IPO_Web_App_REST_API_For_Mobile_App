from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IPOViewSet, IPODocumentViewSet, IPONewsViewSet

router = DefaultRouter()
router.register(r'ipos', IPOViewSet)
router.register(r'documents', IPODocumentViewSet)
router.register(r'news', IPONewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
