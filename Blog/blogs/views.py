from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import BlogForm, ImageForm, Login, UserRegisterForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.forms import modelformset_factory
from .models import Image, BlogModel, Profile, User
from django.views.generic import ListView, DetailView
# Create your views here.

def post(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=2)
    if request.method == 'POST':
        post_form = BlogForm(request.POST)
        form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if post_form.is_valid() and form_set.is_valid() and request.user.is_authenticated:
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for form in form_set.cleaned_data:
                if form:
                    image = form['image']
                    photo = Image(post=post, image=image)
                    photo.save()
            return HttpResponseRedirect('/')
    else:
        post_form = BlogForm()
        form_set = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'site/blog_post.html', context={'post_form': post_form, 'form_set': form_set})




class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'site/main_page.html')

class BlogList(ListView):
    model = BlogModel
    template_name = 'site/blog_list.html'
    context_object_name = 'blog'

class BlogDetail(DetailView):
    model = BlogModel
    template_name = 'site/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = Image.objects.filter(post__pk=self.kwargs['pk'])
        context['post_image'] = ImageForm
        return context




class UserLogin(LoginView):
    template_name = 'site/login.html'


def register(request):
    if request.method =='POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'site/register_ok.html', context={'new_user':new_user})
    else:
        user_form = UserRegisterForm()

    return render(request, 'site/register.html', context={'user_form':user_form})


# class BlogPost(View):
#     def get(self, request):
#         blog_form = BlogForm()
#         return render(request, 'site/blog_post.html', context={'blog_form':blog_form})
#
#     def post(self, request, *args, **kwargs):
#         blog_form = BlogForm(request.POST)
#         if blog_form.is_valid():
#             post = blog_form.save(commit=False)
#             post.user = request.user
#             blog_form.user = request.user
#             post.save()
#             return render(request, 'site/main_page.html', context={'blog_form':blog_form})
#         else:
#             raise PermissionDenied('Вы не можете добавить новость')

class Loguot(LogoutView):
    next_page = '/'


@login_required
def egit_user(request):
    # user = request.user.get_profile()
    # profile = user.profile
    # form = ProfileForm(instance=profile)
    # if request.user.is_authenticated() and request.user.id == user.id:
    if request.method == 'POST' and request.user.is_authenticated:
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return HttpResponse('Данные измененны')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'site/user_profile.html', context={'form': form})

