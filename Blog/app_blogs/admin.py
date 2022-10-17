from django.contrib import admin
from .models import BlogModel, Image, Profile
# Register your models here.

@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


