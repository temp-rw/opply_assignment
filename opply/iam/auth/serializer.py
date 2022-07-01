from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer


class OpplyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token_data = super().get_token(user)
        user.last_login = timezone.now()
        user.save()
        return token_data


class OpplyTokenRefreshSerializer(TokenRefreshSerializer):
    pass
