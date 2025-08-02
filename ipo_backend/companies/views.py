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
        Authenticated users can create and update companies.
        Only admin users can delete companies.
        Anyone can read company data.
        """
        if self.action == 'destroy':  # Only delete requires admin
            permission_classes = [permissions.IsAdminUser]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]  # Any authenticated user can create/update
        else:
            permission_classes = [permissions.AllowAny]  # Anyone can read
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Set the created_by field when creating a new company"""
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['get'])
    def ipos(self, request, pk=None):
        """Get all IPOs for a specific company"""
        company = self.get_object()
        from ipos.serializers import IPOListSerializer
        ipos = company.ipos.all()
        serializer = IPOListSerializer(ipos, many=True)
        return Response(serializer.data)
