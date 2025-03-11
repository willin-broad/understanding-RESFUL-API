from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/",views.BlogPostlistCreate.as_view(),name="blogpost-view-create",),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="update",
        ),
]