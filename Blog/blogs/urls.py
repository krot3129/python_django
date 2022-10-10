from django.urls import path
from .views import UserLogin, register, MainPage, Loguot, post, BlogList, BlogDetail, egit_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPage.as_view()),
    path('blog', post, name='blog' ),
    path('blog_list', BlogList.as_view()),
    path('blog_list/<int:pk>', BlogDetail.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout', Loguot.as_view()),
    path('register', register, name='register'),
    path('profile', egit_user, name='profile')



]