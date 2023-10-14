from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    header = models.CharField(max_length=150, verbose_name='header', unique=True)
    content = models.TextField(verbose_name='content')
    views_count = models.PositiveIntegerField(verbose_name='views count', default=0)
    image = models.ImageField(verbose_name='preview', upload_to='blog_images', null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.header}'
