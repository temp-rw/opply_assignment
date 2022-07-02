from rest_framework import serializers

from iam.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)
