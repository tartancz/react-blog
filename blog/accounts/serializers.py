from abc import ABC

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(
        max_length=user._meta.get_field("first_name").max_length
    )
    last_name = serializers.CharField(
        max_length=user._meta.get_field("last_name").max_length
    )

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["first_name"] = self.validated_data.get("first_name", "")
        data["last_name"] = self.validated_data.get("last_name", "")
        return data
