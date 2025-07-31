from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.http import HttpResponse, Http404
from .models import IPO, IPODocument, IPONews
from .serializers import (
    IPOListSerializer, IPODetailSerializer, IPOCreateUpdateSerializer,
    IPODocumentSerializer, IPONewsSerializer
)


class IPOFilter:
    """Custom filter for IPO queryset"""
    
    @staticmethod
    def filter_by_status(queryset, status_filter):
        if status_filter == 'upcoming':
            return queryset.filter(open_date__gt=timezone.now().date())
        elif status_filter == 'open':
            today = timezone.now().date()
            return queryset.filter(open_date__lte=today, close_date__gte=today)
        elif status_filter == 'closed':
            return queryset.filter(close_date__lt=timezone.now().date(), status__in=['CLOSED', 'LISTED'])
        elif status_filter == 'listed':
            return queryset.filter(status='LISTED')
        return queryset


class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.select_related('company').prefetch_related('documents', 'news')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['board', 'status', 'is_featured', 'is_recommended', 'company__sector']
    search_fields = ['company__name', 'company__sector', 'company__industry', 'registrar']
    ordering_fields = ['open_date', 'close_date', 'listing_date', 'issue_size', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return IPOListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return IPOCreateUpdateSerializer
        return IPODetailSerializer

    def get_permissions(self):
        """
        Admin users can perform all actions.
        Regular users can only read.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'upload_documents']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by status parameter
        status_filter = self.request.query_params.get('filter_status', None)
        if status_filter:
            queryset = IPOFilter.filter_by_status(queryset, status_filter)
        
        return queryset

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Get upcoming IPOs"""
        upcoming_ipos = IPOFilter.filter_by_status(self.get_queryset(), 'upcoming')
        serializer = IPOListSerializer(upcoming_ipos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def open(self, request):
        """Get currently open IPOs"""
        open_ipos = IPOFilter.filter_by_status(self.get_queryset(), 'open')
        serializer = IPOListSerializer(open_ipos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured IPOs"""
        featured_ipos = self.get_queryset().filter(is_featured=True)
        serializer = IPOListSerializer(featured_ipos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search IPOs by company name or sector"""
        query = request.query_params.get('q', '')
        if query:
            ipos = self.get_queryset().filter(
                company__name__icontains=query
            ) | self.get_queryset().filter(
                company__sector__icontains=query
            )
        else:
            ipos = self.get_queryset()
        
        serializer = IPOListSerializer(ipos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def upload_documents(self, request, pk=None):
        """Upload RHP/DRHP documents"""
        ipo = self.get_object()
        
        if 'rhp' in request.data:
            ipo.rhp_document = request.data['rhp']
        if 'drhp' in request.data:
            ipo.drhp_document = request.data['drhp']
        
        ipo.save()
        
        return Response({
            'status': 'Documents uploaded successfully',
            'rhp_url': ipo.rhp_document.url if ipo.rhp_document else None,
            'drhp_url': ipo.drhp_document.url if ipo.drhp_document else None
        })

    @action(detail=True, methods=['get'])
    def download_rhp(self, request, pk=None):
        """Download RHP document"""
        ipo = self.get_object()
        if not ipo.rhp_document:
            raise Http404("RHP document not found")
        
        response = HttpResponse(ipo.rhp_document.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{ipo.company.name}_RHP.pdf"'
        return response

    @action(detail=True, methods=['get'])
    def download_drhp(self, request, pk=None):
        """Download DRHP document"""
        ipo = self.get_object()
        if not ipo.drhp_document:
            raise Http404("DRHP document not found")
        
        response = HttpResponse(ipo.drhp_document.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{ipo.company.name}_DRHP.pdf"'
        return response

    @action(detail=True, methods=['delete'])
    def delete_documents(self, request, pk=None):
        """Delete RHP/DRHP documents"""
        ipo = self.get_object()
        doc_type = request.query_params.get('type', '')
        
        if doc_type == 'rhp' and ipo.rhp_document:
            ipo.rhp_document.delete()
            ipo.rhp_document = None
            ipo.save()
            return Response({'status': 'RHP document deleted'})
        elif doc_type == 'drhp' and ipo.drhp_document:
            ipo.drhp_document.delete()
            ipo.drhp_document = None
            ipo.save()
            return Response({'status': 'DRHP document deleted'})
        
        return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)


class IPODocumentViewSet(viewsets.ModelViewSet):
    queryset = IPODocument.objects.all()
    serializer_class = IPODocumentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class IPONewsViewSet(viewsets.ModelViewSet):
    queryset = IPONews.objects.all()
    serializer_class = IPONewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['ipo']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
