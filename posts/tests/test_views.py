from django.test import TestCase, Client
from posts.models import Author, Post


class AuthorViewsTest(TestCase):
    def setUp(self):
        Author.objects.create(nick='nick 1', email='nick_1@sample.com', bio='Some biography 1')
        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/authors/list")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['authors']), 1)
        self.assertIn('aria-disabled="false">nick 1',
                      response.content.decode())


class PostViewsTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Title 1',
                            content="Some content 1",
                            author=Author.objects.create(nick='nick 1', email='nick_1@sample.com'))
        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/posts/list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 1)
        self.assertIn('aria-disabled="false">Title 1',
                      response.content.decode())