from django.urls import path
from .views import CurrentListAPIView, CurrentIdListAPIView


urlpatterns = [
    path('v1/', CurrentListAPIView.as_view(), name='app-list'),
    path('v1/<int:id>/', CurrentIdListAPIView.as_view(), name='app-list-id'),
]
