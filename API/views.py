from rest_framework import generics
from .models import Document, ServiceCategory, Institute, InstituteEvent, Review
from .serializers import DocumentSerializer, ServiceCategorySerializer, InstituteSerializer, InstituteEventSerializer, ReviewSerializer


class ListDocumentAPI(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ListServiceCategoryAPI(generics.ListCreateAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class ServiceCategoryAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class ListInstituteAPI(generics.ListCreateAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class InstituteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class ListInstituteEventAPI(generics.ListCreateAPIView):
    queryset = InstituteEvent.objects.all()
    serializer_class = InstituteEventSerializer


class InstituteEventAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstituteEvent.objects.all()
    serializer_class = InstituteEventSerializer


class ListReviewAPI(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
