from django.contrib import admin
from django.urls import path
from .views import StatusAPIView, StatusCreateAPIView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('/create/', StatusCreateAPIView.as_view()),
    # path('<id>.*/', StatusRetrieveAPIView.as_view()),
    # path('<id>.*/update/', StatusUpsdateAPIView.as_view()),
    # path('<id>.*/delete/', StatusDeleteAPIView.as_view())
]