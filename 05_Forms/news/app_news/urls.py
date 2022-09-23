from django.urls import path
from .views import Main_page, NewsList, NewsLists, NewsDetail, NewsUpdate, Login, Logout, register

urlpatterns = [
    path('', Main_page.as_view()),
    path('news', NewsList.as_view()),
    path('news_list', NewsLists.as_view()),
    path('news_list/<int:pk>', NewsDetail.as_view(), name='news-detail'),
    path('news_list/<int:pk>/edit', NewsUpdate.as_view(), name='news_update'),
    path('login',Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', register, name='register'),


]
