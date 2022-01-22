from rest_framework import serializers
from contact.models import Category


class SendMailSerializer(serializers.Serializer):
    author = serializers.EmailField()
    title = serializers.CharField(max_length=300)
    body = serializers.CharField()
    category = serializers.IntegerField()

    def validate_category(self, value):
        if not Category.objects.filter(pk=value).exists():
            raise serializers.ValidationError('invalid category')
        return value

    def create(self, validated_data):
        return validated_data
