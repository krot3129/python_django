from django.urls import path
from .views import *




urlpatterns = [
    path('register', RegisterUser.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('loguot', Logout.as_view(), name='logout'),
    path('market', MarketView.as_view(), name='market'),
    path('market/<int:pk>', ProductView.as_view(), name='product'),
    path('basket', BasketView.as_view(), name='basket'),
    path('profile', UserLkView.as_view(), name='profile'),
    path('add_balane', AddBalance.as_view(), name='balance'),
    path('', MainPage.as_view(), name='main_page')

]