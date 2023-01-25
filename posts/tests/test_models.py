import datetime

from django.test import TestCase
from posts.models import Author, Post
import pytz
from unittest import mock


class PostModelTest(TestCase):
    def setUp(self):
        mocked = datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            Post.objects.create(title='Title 1',
                        content="Some content 1",
                        author=Author.objects.create(nick='nick 1', email='nick_1@sample.com'))
            Post.objects.create(title='Title 2',
                        content="Some content 2",
                        author=Author.objects.create(nick='nick 2', email='nick_2@sample.com'))

    def test_post_str(self):
        p1 = Post.objects.get(title='Title 1')
        p2 = Post.objects.get(title='Title 2')

        self.assertEquals(str(p1), """Title: Title 1\nContent: Some content 1
Created: 2023-01-01 00:00:00+00:00\nModified: 2023-01-01 00:00:00+00:00""")
        self.assertEquals(str(p2), """Title: Title 2\nContent: Some content 2
Created: 2023-01-01 00:00:00+00:00\nModified: 2023-01-01 00:00:00+00:00""")


class AuthorModelTest(TestCase):
    def setUp(self):
        Author.objects.create(nick='nick 1', email='nick_1@sample.com', bio='Some biography 1')
        Author.objects.create(nick='nick 2', email='nick_2@sample.com', bio='Some biography 2')

    def test_author_str(self):
        a1 = Author.objects.get(nick='nick 1')
        a2 = Author.objects.get(nick='nick 2')

        self.assertEquals(str(a1), "Nick: nick 1, Email: nick_1@sample.com")
        self.assertEquals(str(a2), "Nick: nick 2, Email: nick_2@sample.com")
