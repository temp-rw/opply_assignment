from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from iam.auth.serializer import OpplyTokenObtainPairSerializer, OpplyTokenRefreshSerializer


@extend_schema(
    tags=["Iam"]
)
class OpplyTokenObtainPairView(TokenObtainPairView):
    serializer_class = OpplyTokenObtainPairSerializer

@extend_schema(
    tags=["Iam"]
)
class OpplyTokenRefreshView(TokenRefreshView):
    serializer_class = OpplyTokenRefreshSerializer
