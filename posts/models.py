from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ['-id']

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nCreated: {self.created}\nModified: {self.modified}"


class Author(models.Model):
    class Meta:
        ordering = ['id']

    nick = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Nick: {self.nick}, Email: {self.email}"