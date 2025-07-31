from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    total_ipos = serializers.ReadOnlyField()
    upcoming_ipos = serializers.ReadOnlyField()
    
    class Meta:
        model = Company
        fields = [
            'id', 'name', 'description', 'sector', 'industry', 
            'website', 'established_year', 'headquarters', 'logo',
            'total_ipos', 'upcoming_ipos', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'total_ipos', 'upcoming_ipos']

    def create(self, validated_data):
        # Set the created_by field to the current user
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Set the updated_by field to the current user
        validated_data['updated_by'] = self.context['request'].user
        return super().update(instance, validated_data)


class CompanyListSerializer(serializers.ModelSerializer):
    total_ipos = serializers.ReadOnlyField()
    upcoming_ipos = serializers.ReadOnlyField()
    
    class Meta:
        model = Company
        fields = [
            'id', 'name', 'sector', 'industry', 'logo',
            'total_ipos', 'upcoming_ipos'
        ]
