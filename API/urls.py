from django.urls import path
from .views import DocumentAPI, ServiceCategoryAPI, InstituteAPI, InstituteEventAPI, ReviewAPI
from .views import ListDocumentAPI, ListServiceCategoryAPI, ListInstituteAPI, ListInstituteEventAPI, ListReviewAPI

urlpatterns = [
    path('api/v1/institutes', ListInstituteAPI.as_view(), name="institutesAPI"),
    path('api/v1/events', ListInstituteEventAPI.as_view(), name="eventsAPI"),
    path('api/v1/categories', ListServiceCategoryAPI.as_view(), name="categoriesAPI"),
    path('api/v1/documents', ListDocumentAPI.as_view(), name="documentsAPI"),
    path('api/v1/reviews', ListReviewAPI.as_view(), name="reviewsAPI"),
    path('api/v1/institutes/<int:pk>/', InstituteAPI.as_view(), name="institutesAPI"),
    path('api/v1/events/<int:pk>/', InstituteEventAPI.as_view(), name="eventsAPI"),
    path('api/v1/categories/<int:pk>/', ServiceCategoryAPI.as_view(), name="categoriesAPI"),
    path('api/v1/documents/<int:pk>/', DocumentAPI.as_view(), name="documentsAPI"),
    path('api/v1/reviews/<int:pk>/', ReviewAPI.as_view(), name="reviewsAPI"),
]
