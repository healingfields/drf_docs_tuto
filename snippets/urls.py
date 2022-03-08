from django.urls import path
from .views import (
    SnippetDetailsUsingGenericCBV,
    SnippetHighlight,
    SnippetLisUsingCBV,
    SnippetListUsingGenericCBV,
    UserDetails,
    UserList,
    api_root,
    snippet_details,
    snippet_details_using_decorator,
    snippet_list,
    snippet_list_using_decorator,
    SnippetDetailsUsingCBV,
)
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # using functional views
    # path("snippets/", snippet_list, name="snippet_list"),
    # path("snippets/<int:pk>/", snippet_details, name="snippet_details"),
    # using functional views with the request and response provided by DRF
    # path("snippets/", snippet_list_using_decorator, name="snippet_list"),
    # path("snippets/<int:pk>/", snippet_details_using_decorator, name="snippet_details"),
    # using CBV
    # path("snippets/", SnippetLisUsingCBV.as_view(), name="snippet_list"),
    # path(
    #     "snippets/<int:pk>/", SnippetDetailsUsingCBV.as_view(), name="snippet_details"
    # ),
    # using generic CBV
    path("snippets/", SnippetListUsingGenericCBV.as_view(), name="snippet-list"),
    path(
        "snippets/<int:pk>/",
        SnippetDetailsUsingGenericCBV.as_view(),
        name="snippet-detail",
    ),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetails.as_view(), name="user-detail"),
    path("", api_root),
    path(
        "snippets/<int:pk>/highlight/",
        SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
]


# support for multiples formats
urlpatterns = format_suffix_patterns(urlpatterns)
