from rest_framework import serializers
from posts.models import Posts


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(
        required=False, allow_blank=True, max_length=280)

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
