from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Status
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostListView(ListView):
    template_name = "posts/list.html"  
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs): #kwargs=keywarod argument, dictionary retriving
        context=super().get_context_data(**kwargs)
        published = Status.objects.get(name="published")
        context["post_list"]=(
            Post.objects
            .filter(status=published)
            .order_by("created_on").reverse()
        )
        return context
    

    
class DraftPostListView(ListView):
    template_name="posts/list.html"
    model=Post

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        draft=Status.objects.get(name="draft")
        context["post_list"]=(
            Post.objects
            .filter(status=draft)
            .filter(author=self.request.user)
            .order_by("created_on").reverse()
        )
        return context


class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name="posts/list.html"
    model=Post

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        archived=Status.objects.get(name="archived")
        context["post_list"]=(
            Post.objects
            .filter(status=archived)
            .order_by("created_on").reverse()
        )    
        return context



class PostCreateView(LoginRequiredMixin, CreateView): #superClass is stay on the right--CreateView
    template_name = "posts/new.html"  
    model = Post
    fields = ["title", "subtitle", "body","status"]
    success_url = reverse_lazy('list') 

    def form_valid(self, form):
        form.instance.author=self.request.user
        # form.instance.status=Status.objects.get(name="pusblished")
        return super().form_valid(form)



class PostDetailView(DetailView):
    template_name = "posts/detail.html"  
    model = Post
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html" 
    model = Post
    fields = ["title", "subtitle","body", "status"]

    def test_func(self):
        post=self.get_object()
        return post.author==self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html" 
    model = Post
    success_url = reverse_lazy('list') 

    def test_func(self):
        post=self.get_object()
        return post.author==self.request.user
