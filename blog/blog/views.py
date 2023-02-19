from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy                          # new
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):   # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):   # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):    # new
    model = Post
    template_name = 'post_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
