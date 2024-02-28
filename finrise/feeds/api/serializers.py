from rest_framework import serializers

from feeds.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]

    # hashing the password

    def validate_password(self, value: str) -> str:
        return make_password(value)