from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from .forms import NewsForm, CommentForm
from .models import News, Comment

class Main_page(View):

    def get(self, reuests, *args, **kwargs):
        return render(reuests, 'pages/main_page.html')




class NewsList(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news_list.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'pages/main_page.html', context={'news_form': news_form})





class NewsLists(ListView):
    model = News
    template_name = 'pages/news_lists.html'
    context_object_name = 'news_lists'
    queryset = News.objects.all()



class NewsDetail(DetailView):
    model = News


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comment'] = Comment.objects.all()
        data['form'] = CommentForm
        return data

    def post(self, request, pk):
        com_form = CommentForm(request.POST)
        if com_form.is_valid():
            Comment.objects.create(**com_form.cleaned_data)
            # pk.Comment.objects.id()

            return HttpResponseRedirect('/news_list')
        return render(request, 'pages/news_detail.html', context={'com_form': com_form})





class NewsUpdate(UpdateView):
    model = News
    template_name = 'pages/news_up.html'
    fields = ['name', 'content']


