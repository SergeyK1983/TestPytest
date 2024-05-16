from rest_framework import serializers
from .models import CurrentModel, RelCurrent


class RelCurrentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelCurrent
        fields = ['text']


class CurrentSerializer(serializers.ModelSerializer):
    current = RelCurrentSerializer(many=True)

    class Meta:
        model = CurrentModel
        fields = ['id', 'name', 'description', 'count', 'current']
