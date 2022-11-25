from django.contrib import admin
from .models import *



@admin.register(MarketModel)
class MarketAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(LkUser)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(BasketModel)
class BasketAdmin(admin.ModelAdmin):
    pass

