import random

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ..models import BlogModel, Profile

POST = 10

class TestModel(TestCase):
    def test_fields_model(self):
        blog = BlogModel()
        blog.title = 'Test title'
        blog.content = 'Test content'
        blog.created_at = timezone.now()
        blog.save()
        response = BlogModel.objects.get(pk=1)
        self.assertEqual(response, blog)


