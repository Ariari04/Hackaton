from rest_framework import serializers
from .models import Document, ServiceCategory, Institute, InstituteEvent


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'


class InstituteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteEvent
        fields = '__all__'
