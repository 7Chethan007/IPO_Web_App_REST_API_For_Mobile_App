from rest_framework import serializers
from .models import IPO, IPODocument, IPONews
from companies.serializers import CompanyListSerializer


class IPODocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPODocument
        fields = ['id', 'document_type', 'title', 'file', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class IPONewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPONews
        fields = ['id', 'title', 'content', 'source', 'source_url', 'created_at']
        read_only_fields = ['id', 'created_at']


class IPOListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_logo = serializers.ImageField(source='company.logo', read_only=True)
    price_range = serializers.ReadOnlyField()
    is_open = serializers.ReadOnlyField()
    days_to_open = serializers.ReadOnlyField()
    days_to_close = serializers.ReadOnlyField()
    
    class Meta:
        model = IPO
        fields = [
            'id', 'company_name', 'company_logo', 'issue_size',
            'price_range_min', 'price_range_max', 'price_range',
            'open_date', 'close_date', 'listing_date', 'board',
            'status', 'lot_size', 'listing_gains', 'is_featured',
            'is_recommended', 'is_open', 'days_to_open', 'days_to_close'
        ]


class IPODetailSerializer(serializers.ModelSerializer):
    company = CompanyListSerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)
    documents = IPODocumentSerializer(many=True, read_only=True)
    news = IPONewsSerializer(many=True, read_only=True)
    price_range = serializers.ReadOnlyField()
    is_open = serializers.ReadOnlyField()
    days_to_open = serializers.ReadOnlyField()
    days_to_close = serializers.ReadOnlyField()
    
    class Meta:
        model = IPO
        fields = [
            'id', 'company', 'company_id', 'issue_size',
            'price_range_min', 'price_range_max', 'price_range',
            'listing_price', 'open_date', 'close_date', 'listing_date',
            'board', 'status', 'lot_size', 'total_subscription',
            'retail_subscription', 'qib_subscription', 'nii_subscription',
            'rhp_document', 'drhp_document', 'registrar', 'lead_managers',
            'listing_gains', 'current_price', 'is_featured', 'is_recommended',
            'documents', 'news', 'is_open', 'days_to_open', 'days_to_close',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'price_range', 'is_open', 'days_to_open', 'days_to_close']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super().update(instance, validated_data)


class IPOCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = [
            'company', 'issue_size', 'price_range_min', 'price_range_max',
            'listing_price', 'open_date', 'close_date', 'listing_date',
            'board', 'status', 'lot_size', 'total_subscription',
            'retail_subscription', 'qib_subscription', 'nii_subscription',
            'registrar', 'lead_managers', 'listing_gains', 'current_price',
            'is_featured', 'is_recommended'
        ]

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super().update(instance, validated_data)
