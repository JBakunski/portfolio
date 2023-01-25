from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request=request, template_name='posts/posts_list.html', context={'posts': posts,
                                                                                   'title': 'Posts list'})


def post_details(request, id):
    return render(request=request, template_name='posts/post_details.html', context={'post': Post.objects.get(id=id),
                                                                                     'title': 'Post detail'})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, template_name='posts/authors_list.html', context={'authors': authors, 'title': 'Authors list'})


def author_details(request, id):
    return render(request, template_name='posts/author_details.html', context={'author': Author.objects.get(id=id),
                                                                               'title': 'Author details'})


def add_author(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, template_name='posts/author_form.html', context={'form': form})


def add_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, template_name='posts/post_form.html', context={'form': form})