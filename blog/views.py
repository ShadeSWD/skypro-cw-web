from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import *
from blog.forms import PostForm


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog.html"
    context_object_name = 'posts'
    queryset = Post.objects.all()


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        new_post = form.save()
        new_post.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        new_post = form.save()
        new_post.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:blog_list")
