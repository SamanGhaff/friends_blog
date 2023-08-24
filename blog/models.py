from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from . import managers
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="articles")
    category = models.ManyToManyField(Category, blank=True, related_name="articles")
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    floatfield = models.FloatField(default=1)
    # myfile = models.BinaryField(null=True)
    myfile = models.FileField(upload_to='test', null=True, blank=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)
    objects = models.Manager()
    custom_manager = managers.ArticleManager()

    class Meta:
        ordering = ('-created',)

    #     # ordering = ('created',)
    #     # ordering = ('-updated',)
    #     # ordering = ('-updated', '-created')
    #     # verbose_name = 'post'
    #     # verbose_name_plural = 'articles'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]


# class New(models.Model):
#     title = models.CharField(max_length=30)
#     des = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.title = self.title.replace(' ', '-')
#         super(New, self).save(args, kwargs)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        ordering = ('-created_at',)
