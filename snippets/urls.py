from django.urls import path
from .views import (
    snippet_details,
    snippet_details_using_decorator,
    snippet_list,
    snippet_list_using_decorator,
)
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path("snippets/", snippet_list, name="snippet_list"),
    # path("snippets/<int:pk>/", snippet_details, name="snippet_details"),
    path("snippets/", snippet_list_using_decorator, name="snippet_list"),
    path("snippets/<int:pk>/", snippet_details_using_decorator, name="snippet_details"),
]

# support for multiples formats
urlpatterns = format_suffix_patterns(urlpatterns)
