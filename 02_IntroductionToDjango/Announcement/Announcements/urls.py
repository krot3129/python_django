from django.urls import path
from .import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path("Announcements/", views.Announcements_list, name='Announcements_list'),
    path('Announcements_1', views.Announcements_1, name='Announcements_1'),
    path('Announcements_2', views.Announcements_2, name='Announcements_2'),
    path('Announcements_3', views.Announcements_3, name='Announcements_3'),
    path('Announcements_4', views.Announcements_4, name='Announcements_4'),
    path('Announcements_5', views.Announcements_5, name='Announcements_5')
]