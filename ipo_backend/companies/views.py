from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company
from .serializers import CompanySerializer, CompanyListSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sector', 'industry']
    search_fields = ['name', 'description', 'sector', 'industry']
    ordering_fields = ['name', 'created_at', 'established_year']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyListSerializer
        return CompanySerializer

    def get_permissions(self):
        """
        Admin users can perform all actions.
        Regular users can only read.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get'])
    def ipos(self, request, pk=None):
        """Get all IPOs for a specific company"""
        company = self.get_object()
        from ipos.serializers import IPOListSerializer
        ipos = company.ipos.all()
        serializer = IPOListSerializer(ipos, many=True)
        return Response(serializer.data)
