from django import forms
from .models import News, Comment
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'content', 'active', 'tag']
    # name = forms.CharField(label='Заголовок')
    # content = forms.CharField(widget = forms.Textarea(attrs={'cols':60, 'rows':10 }), label='Содержание новости')
    # active = forms.BooleanField(label='Статус')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'anon_user']



class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пороля', widget=forms.PasswordInput)
    phone = forms.CharField(label='Телефон')
    city = forms.CharField(label='Город')
    # news_count = forms.IntegerField(label='Кол-во новостей')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


