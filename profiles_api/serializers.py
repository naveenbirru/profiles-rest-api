from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing out APIview"""
    name = serializers.CharField(max_length=10)
