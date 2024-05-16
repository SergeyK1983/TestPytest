from rest_framework import serializers
from .models import CurrentModel, RelCurrent


class RelCurrentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelCurrent
        fields = ["text"]


class CurrentSerializer(serializers.ModelSerializer):
    current = RelCurrentSerializer(many=True)

    class Meta:
        model = CurrentModel
        fields = ["id", "name", "description", "count", "current"]


class CurrentCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrentModel
        fields = ["name", "description", "count"]

    def create(self, validated_data):
        instance = CurrentModel.objects.create(**validated_data)
        return instance
