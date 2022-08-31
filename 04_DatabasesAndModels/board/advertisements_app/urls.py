from django.urls import path
from . import views
from .views import AdvertisementListViev, AdvertisementDetailView
urlpatterns = [
    path('', views.Main_page.as_view()),
    path('advertisements', AdvertisementListViev.as_view(), name='advertisement'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement-detail')

]
