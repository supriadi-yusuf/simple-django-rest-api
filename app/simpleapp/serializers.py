from rest_framework import serializers

class CalculateSerializer(serializers.Serializer):
    """input calculator"""

    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)