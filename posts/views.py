from django.shortcuts import render
from posts.models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request=request, template_name='posts/list.html', context={'posts': posts, 'title': 'Posts list'})


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request=request, template_name='posts/details.html', context={'post': post})



