from django.urls import path
from posts import views
from .views import PostCreateView, PostListView,PostDetailView,PostUpdateView,PostDeleteView

urlpatterns=[
    path("",views.PostListView.as_view(), name="list"),
    path("new/",PostCreateView.as_view(), name="new"), 

    path("<int:pk>/",views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/",views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/",views.PostDeleteView.as_view(), name="delete"),
]