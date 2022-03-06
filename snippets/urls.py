from urllib.parse import urlparse
from django.urls import path
from .views import snippet_details, snippet_list


urlpatterns = [
    path("snippets/", snippet_list, name="snippet_list"),
    path("snippets/<int:pk>/", snippet_details, name="snippet_details"),
]
