from django.urls import path, include

from api.v1 import auth, docs

app_name = 'api'

urlpatterns = [
    path('auth/', include(auth.urlpatterns)),
    path('docs/', include(docs.urlpatterns)),
]
