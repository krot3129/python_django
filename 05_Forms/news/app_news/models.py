from django.db import models
#
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser


class News(models.Model):
    # STATUS_CHOICE ={'a':True,'n':False}

    objects = None
    name = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active = models.BooleanField(default=None, verbose_name='Статус')
    # users = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, verbose_name='Пользователь')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])


class Comment(models.Model):
    objects = None
    name = models.CharField(max_length=50, verbose_name='Заголовок')
    email = models.EmailField(verbose_name='Эл.почта')
    body = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    active = models.BooleanField(default=True, verbose_name='Статус')
    news_com = models.ForeignKey('News', on_delete=models.CASCADE, default=None)
    users = models.ForeignKey(User, AnonymousUser, default=None, blank=True, null=True)
    anon_user = models.CharField(max_length=50, verbose_name='Имя анонима', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('news-detail/<int:pk>', kwargs={'news_com': self.pk})

    def get_description(self):
        return self.body[:15]

    get_description.short_description = 'Description'




#
# class User(models.Model):
#     name = models.CharField(max_length=30, verbose_name='Имя')
#     email = models.EmailField(verbose_name='Электронная почта')
#
#     def __str__(self):
#         return self.name

