from django.db import models
from django.contrib.auth.models import User


from django.urls import reverse

class BlogModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(max_length=500, verbose_name='Содержание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    class Meta:
        ordering = ['created_at']


    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    about = models.TextField(blank=True, verbose_name='Информация о себе')
    email = models.EmailField(max_length=20, verbose_name='Эл.Почта')
    city = models.CharField(max_length=20, verbose_name='Город')
    avatar = models.ImageField(upload_to='media/', blank=True, null=True)




class Image(models.Model):
    objects = None
    image = models.ImageField(upload_to='media', blank=True, verbose_name='Изображение')
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog-detail/<int:pk>', kwargs={'post': self.pk})






