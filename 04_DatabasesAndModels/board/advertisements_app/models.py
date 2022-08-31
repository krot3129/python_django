import datetime

from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    date_in = models.DateField(auto_now_add=True)
    date_out = models.DateField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type = models.ForeignKey('Types', default=None, null=True, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.TextField(max_length=30, verbose_name='Электронная почта')
    phone = models.IntegerField(verbose_name='Телефон')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Types(models.Model):
    name = models.CharField(max_length=100, db_index=True, default=None, null=True)

    def __str__(self):
        return self.name