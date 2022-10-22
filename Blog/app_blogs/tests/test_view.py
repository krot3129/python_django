from django.test import TestCase, Client
from ..views import *
from django.urls import reverse, resolve
from django.utils import timezone
from ..models import BlogModel
class TestPost(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='TestUser', email='test@test.ru')
        self.user.set_password('12345')
        self.user.save()

    def test_post_view(self):
        post = BlogModel.objects.create(title='test_title', content='some text', user=self.user, created_at=timezone.now())
        self.assertEqual(post.title, 'test_title')

    

    def test_authenticate_user(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)


