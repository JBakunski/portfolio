from django.contrib import admin
from posts.models import Author, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nick', 'email']


admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'modified']
    list_filter = ['created']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
