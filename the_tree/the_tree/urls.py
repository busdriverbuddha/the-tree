# the_tree/urls.py

from django.urls import path, include


urlpatterns = [
    path('api-auth/', include("rest_framework.urls")),
    path('', include('budget.urls')),
]
