from django.urls import path
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularYAMLAPIView,
    SpectacularRedocView
)

urlpatterns = [
    path('swagger.yaml', SpectacularYAMLAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]