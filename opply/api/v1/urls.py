from django.urls import path, include

from api.v1 import auth

app_name = 'api'

urlpatterns = [
    path('auth/', include(auth.urlpatterns))
]