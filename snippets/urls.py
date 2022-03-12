from unicodedata import name
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
    SnippetViewSet,
    UserViewSet,
)
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
snippet_highlight = SnippetViewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
)
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})


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
    # path("snippets/", SnippetListUsingGenericCBV.as_view(), name="snippet-list"),
    # path(
    #     "snippets/<int:pk>/",
    #     SnippetDetailsUsingGenericCBV.as_view(),
    #     name="snippet-detail",
    # ),
    # path("users/", UserList.as_view(), name="user-list"),
    # path("users/<int:pk>/", UserDetails.as_view(), name="user-detail"),
    # path("", api_root),
    # path(
    #     "snippets/<int:pk>/highlight/",
    #     SnippetHighlight.as_view(),
    #     name="snippet-highlight",
    # ),
    path("", api_root),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
]


# support for multiples formats
urlpatterns = format_suffix_patterns(urlpatterns)
