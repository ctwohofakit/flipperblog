from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"  
    model = Post
    context_object_name = "posts"

class PostCreateView(CreateView):
    template_name = "posts/new.html"  
    model = Post
    fields = ["title", "subtitle", "body", "author"]
    success_url = reverse_lazy("list")

class PostDetailView(DetailView):
    template_name = "posts/detail.html"  
    model = Post

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html" 
    model = Post
    fields = ["title", "subtitle","body", "author"]
    success_url = reverse_lazy("list")

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html" 
    model = Post
    success_url = reverse_lazy("list")
