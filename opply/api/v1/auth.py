from django.urls import path

from iam.auth.views import OpplyTokenObtainPairView, OpplyTokenRefreshView

urlpatterns = [
    path('token', OpplyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', OpplyTokenRefreshView.as_view(), name='token_refresh'),
]