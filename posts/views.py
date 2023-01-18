from django.shortcuts import render
from posts.models import Post, Author


def posts_list(request):
    posts = Post.objects.all()
    return render(request=request, template_name='posts/posts_list.html', context={'posts': posts, 'title': 'Posts list'})


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request=request, template_name='posts/post_details.html', context={'post': post, 'title': 'Post detail'})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, template_name='posts/authors_list.html', context={'authors': authors, 'title': 'Authors list'})


def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(request, template_name='posts/author_details.html', context={'author': author, 'title': 'Author details'})
