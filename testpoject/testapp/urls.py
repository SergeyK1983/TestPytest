from django.urls import path
from .views import CurrentListAPIView, CurrentIdListAPIView, CurrentCreateAPIView


urlpatterns = [
    path('v1/', CurrentListAPIView.as_view(), name='app-list'),
    path('v1/<int:id>/', CurrentIdListAPIView.as_view(), name='app-list-id'),
    path('v1/current/', CurrentCreateAPIView.as_view(), name='current-create'),
]
