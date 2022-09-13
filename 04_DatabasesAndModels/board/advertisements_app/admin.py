from django.contrib import admin
from .models import Advertisement, Author, Category, Types
# Register your models here.

class Advertisementline(admin.TabularInline):
    model = Author

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category']
    search_fields = ['description']
    inlines = [Advertisementline]


class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

class CategoryAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Author, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Types, TypeAdmin)