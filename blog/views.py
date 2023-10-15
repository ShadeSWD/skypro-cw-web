from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import *
from blog.forms import PostForm


class BlogListView(ListView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['posts'] = Post.objects.all()
        return context_data


class BlogCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        new_post = form.save()
        new_post.owner = self.request.user
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
