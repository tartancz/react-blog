from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Post


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "last_name"]


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    author = NestedUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_author(self):
        user = self.context.get("request").user
        return user

    def create(self, validated_data):
        validated_data["author"] = self.get_author()
        return Post.objects.create(**validated_data)
