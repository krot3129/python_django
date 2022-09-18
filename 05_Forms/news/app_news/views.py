from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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
            news_form.save()
            # News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'pages/main_page.html', context={'news_form': news_form})





class NewsLists(ListView):
    model = News
    template_name = 'pages/news_lists.html'
    context_object_name = 'news_lists'
    queryset = News.objects.all()



class NewsDetail(DetailView):
    model = News
    context_object_name = 'news'



    def get_context_data(self,  **kwargs):
        data = super().get_context_data(**kwargs)
        data['comment'] = Comment.objects.filter(news_com__pk=self.kwargs['pk'])
        data['form'] = CommentForm
        return data

    # def get_queryset(self):
    #     return Comment.objects.filter(news_com__pk=self.kwargs['pk'])

    def post(self, request, pk):
        com_form = CommentForm(request.POST)
        if com_form.is_valid() and request.user.is_authenticated :
            new_comment = com_form.save(commit=False)
            new_comment.data = com_form.cleaned_data
            new_comment.news_com = self.get_object()
            new_comment.users = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('news-detail', args=[pk]))
        elif not request.user.is_authenticated:
            new_comment = com_form.save(commit=False)
            new_comment.data = com_form.cleaned_data
            new_comment.news_com = self.get_object()
            new_comment.save()
            return HttpResponseRedirect(reverse('news-detail', args=[pk]))
        return render(request, 'app_news/news_detail.html', context={'com_form': com_form})





class NewsUpdate(UpdateView):
    model = News
    template_name = 'pages/news_up.html'
    fields = ['name', 'content']


class Login(LoginView):
    template_name = 'pages/login.html'

class Logout(LogoutView):

    next_page = '/'
