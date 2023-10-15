from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('post/create', BlogCreateView.as_view(), name='blog_create'),
    path('post/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
]
