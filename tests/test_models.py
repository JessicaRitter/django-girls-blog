from django.test import TestCase
from django.utils import timezone
from blog.models import Post


class TestTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_false_is_false(self):
        self.assertFalse(False)

    def test_false_is_true(self):
        self.assertTrue(False)


class TestPosts(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(author='admin', title="this is a post", text='length is important here',
                                   created_date=timezone.now, published_date=timezone.now)

    def setUpPost(self):
        self.assertContains(Post.author,Post.title,Post.text,Post.created_date,Post.published_date)

        self.assertContains(Post.text, 'length is important here')



