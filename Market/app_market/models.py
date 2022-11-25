from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MarketModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название магазина')
    dicription = models.TextField(max_length=200, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])



class ProductModel(models.Model):
    market = models.ForeignKey(MarketModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Название продукта')
    price = models.DecimalField(default=0, max_digits=10, decimal_places= 2,verbose_name='Цена')
    in_stock = models.IntegerField(verbose_name='Наличие на складе')


    def __str__(self):
        return self.name

class BasketModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')


class LkUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    balance = models.PositiveIntegerField(default=0, verbose_name='Баланс')
    status = models.CharField(verbose_name='Статус пользователя', max_length=20, default='Без статуса')


    def update_status(self):
        if self.balance < 100:
            self.status = 'Новый пользователь'
        elif self.balance < 500:
            self.status = 'Опытный пользователь'
        else:
            self.status = 'Круче чем Чак'
        return self.status




