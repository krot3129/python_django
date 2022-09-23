from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from .forms import NewsForm, CommentForm, UserRegisterForm
from .models import News, Comment, Profile


class Main_page(View):

    def get(self, reuests, *args, **kwargs):
        return render(reuests, 'pages/main_page.html')


class NewsList(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news_list.html', context={'news_form': news_form})

    def post(self, request):
        if request.user.has_perm('app_news.add_news'):
            news_form = NewsForm(request.POST)
            if news_form.is_valid():
                news_form.save()
            # News.objects.create(**news_form.cleaned_data)
                return HttpResponseRedirect('/')
            return render(request, 'pages/main_page.html', context={'news_form': news_form})

        else:
            raise PermissionDenied()


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


def register(request):
    if request.method =='POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            city = user_form.cleaned_data.get('city')
            phone = user_form.cleaned_data.get('phone')
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(users=new_user, city=city, phone=phone)
            new_user.save()
            return render(request, 'pages/register_ok.html', context={'new_user':new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'pages/register.html', context={'user_form':user_form})


