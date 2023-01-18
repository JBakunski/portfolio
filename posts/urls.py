from django.urls import path
from .views import posts_list, post_details

app_name = 'posts'
urlpatterns = [
    path('posts/list/', posts_list, name='list'),
    path('post/<int:id>', post_details, name='details')
]
