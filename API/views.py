from rest_framework import generics
from .models import Document, ServiceCategory, Institute, InstituteEvent
from .serializers import DocumentSerializer, ServiceCategorySerializer, InstituteSerializer, InstituteEventSerializer


class DocumentAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ServiceCategoryAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class InstituteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class InstituteEventAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstituteEvent.objects.all()
    serializer_class = InstituteEventSerializer
