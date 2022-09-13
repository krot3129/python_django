from django.contrib import admin

from .models import Comment, News, User



class CommentInLine(admin.TabularInline):
    model = Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['del_for_admin']
    list_display = ('name', 'email', 'created', 'active', 'get_description')
    list_filter = ('active', 'created', 'updated', 'users')
    search_fields = ('name', 'email', 'body')

    def del_for_admin(self, request, queryset):
        queryset.update(body='Удалено Администратором')


    del_for_admin.short_description ='Удаленно Администратором'



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    actions = ['active_mark', 'not_active_mark']
    list_display = ('id', 'name', 'active', 'created_date', 'users', 'update')
    list_filter = ['active']
    inlines = [CommentInLine]

    def active_mark(self, request, queryset):
        queryset.update(active=True)

    def not_active_mark(self, request, queryset):
        queryset.update(active=False)

    active_mark.short_description = 'Активно'
    not_active_mark.short_description = 'Не активно'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass