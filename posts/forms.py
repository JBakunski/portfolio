from django.forms import ModelForm
from .models import Author, Post


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']