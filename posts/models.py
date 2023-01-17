from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE
    )


class Author(models.Model):
    nick = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
