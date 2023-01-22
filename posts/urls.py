from django.urls import path
from .views import posts_list, post_details, authors_list, author_details, add_author, add_post

app_name = 'posts'
urlpatterns = [
    path('posts/list/', posts_list, name='posts_list'),
    path('post/<int:id>', post_details, name='post_details'),
    path('authors/list', authors_list, name='authors_list'),
    path('author/<int:id>', author_details, name='author_details'),
    path('author/form', add_author, name='author_form'),
    path('post/form', add_post, name='post_form'),
]
