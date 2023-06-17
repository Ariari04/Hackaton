from django.urls import path

from .views import DetailPromptResponse, PromtResponseAPIView

urlpatterns = [
    path("prompts", PromtResponseAPIView.as_view(), name="prompt_list"),
    path("prompts/<int:pk>/", DetailPromptResponse.as_view(), name="prompt_detail"),
]
