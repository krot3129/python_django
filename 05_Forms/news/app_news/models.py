from django.db import models
#
from django.urls import reverse


class News(models.Model):
    objects = None
    name = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    users = models.ForeignKey('User', on_delete=models.CASCADE, default=None, null=True)
    news_com = models.ForeignKey('Comment', on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])


class Comment(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('news-detail/<int:pk>', args=[str(self.id)])





class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.name

