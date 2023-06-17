from django.urls import path
from .views import DocumentAPI, ServiceCategoryAPI, InstituteAPI, InstituteEventAPI

urlpatterns = [
    path('api/v1/institutes', InstituteAPI.as_view(), name="institutesAPI"),
    path('api/v1/events', InstituteEventAPI.as_view(), name="eventsAPI"),
    path('api/v1/categories', ServiceCategoryAPI.as_view(), name="categoriesAPI"),
    path('api/v1/documents', DocumentAPI.as_view(), name="documentsAPI"),
]
