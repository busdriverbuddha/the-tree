from django.urls import path, include


urlpatterns = [
    path('api-auth/', include("rest_Framework.urls")),
    path('', include('budget.urls')),
]
