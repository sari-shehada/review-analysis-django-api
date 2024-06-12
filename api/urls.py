from django.urls import path
from .views import ReviewAnalysisAPIView

urlpatterns = [
    path('', ReviewAnalysisAPIView.as_view()),
]
