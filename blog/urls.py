from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('post/create', BlogCreateView.as_view(), name='blog_create'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
]
