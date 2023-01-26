from posts.models import Author, Post
from posts.forms import AuthorForm, PostForm
from django.test import TestCase


class AuthorFormTest(TestCase):
    def test_author_form_save_correct_data(self):
        data = {"nick": 'nick 1',
                "email": 'nick1@sample.com',
                "bio": 'Some biography'}
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEquals(a.nick, 'nick 1')
        self.assertIsNotNone(a.id)

    def test_author_form_empty(self):
        form = AuthorForm(data={})

        self.assertFalse(form.is_valid())

        self.assertEqual(form.errors['nick'], ['This field is required.'])
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_author_form_invalid_input(self):
        data = {"nick": 'nick 1',
                "email": 111,
                "bio": 'Some biography'}
        form = AuthorForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])


class PostFormTest(TestCase):
    def test_post_form_save_correct_data(self):
        a = Author.objects.create(nick='nick 1', email='nick1@someemail.com')
        data = {"title": 'Title 1',
                "content": 'Some content 1',
                "author": a}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEquals(p.title, 'Title 1')
        self.assertIsNotNone(p.id)

    def test_post_missing_author(self):
        data = {"title": 'Title 1',
                "content": 'Some content 1',
                "author": ''}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['author'], ['This field is required.'])
