from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing the API View

    Args:
        serializers (class): django rest_framework class for serializing inputs to save in the database
    """

    name = serializers.CharField(max_length=10)
