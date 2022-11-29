
from django.urls import path
from .views import CustomTokenObtainPairView, CustomTokenRefreshView


app_name='authentication'
urlpatterns = [
    path('get-token', CustomTokenObtainPairView.as_view(), name='get-token'),
    path('refresh-token', CustomTokenRefreshView.as_view(), name='refresh-token')
]
