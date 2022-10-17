from django.urls import path
from .views import UserLogin, register, MainPage, Loguot, post, BlogList, BlogDetail, egit_user, update_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPage.as_view()),
    path('blog', post, name='blog'),
    path('blog_list', BlogList.as_view(), name='blog-list'),
    path('blog_list/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout', Loguot.as_view(), name='logout'),
    path('register', register, name='register'),
    path('profile', egit_user, name='profile'),
    path('update_post', update_post, name='update_post')



]