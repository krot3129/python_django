from django.shortcuts import render
from django.views.generic import ListView,DetailView
from advertisements_app.models import Advertisement
from django.views import View


class Main_page(View):
    """
    Класс который описывает вид главной страницы сайта
    """

    def get(self, requests):
        return render(requests, 'advertisements_app/main_page.html')

    def post(self, requests):
        return render(requests, 'advertisements_app/main_page.html')

def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements/advertisements.html', {'advertisements':advertisements})

class AdvertisementListViev(ListView):
    model = Advertisement
    template_name = 'advertisements_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]

class AdvertisementDetailView(DetailView):
    model = Advertisement