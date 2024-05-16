from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import CurrentModel
from .serializer import CurrentSerializer, CurrentCreateUpdateSerializer


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


class CurrentCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrentCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
