from rest_framework import generics, permissions
from .models import CurrentModel
from .serializer import CurrentSerializer


class CurrentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrentSerializer
    queryset = CurrentModel.objects.all()


class CurrentIdListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrentSerializer

    def get_queryset(self):
        queryset = CurrentModel.objects.filter(id=self.kwargs["id"])
        return queryset
