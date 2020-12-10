from django.urls import path
from .views import PostCreateView,PostListView,PostUpdateView,PostDetailView,PostDeleteView

urlpatterns=[
     path("new/",PostCreateView.as_view(),name="create-post"),
     path("view/",PostListView.as_view(),name="view-post"),
     path("update/<int:pk>",PostUpdateView.as_view(),name="update-post"),
     path("detail/<int:pk>",PostDetailView.as_view(),name="detail-post"),
     path("delete/<int:pk>",PostDeleteView.as_view(),name="delete-post")
]