from django import forms
from django.contrib.auth.models import User
from .models import *






class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пороля', widget=forms.PasswordInput)
    phone = forms.CharField(label='Телефон')
    city = forms.CharField(label='Город')



    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']






class LkUserForm(forms.Form):
    balance = forms.IntegerField(label='balance')


# class BasketForm(forms.Form):
#     quantity = forms.IntegerField(label='Кол-во товара')
#     product = forms.HiddenInput()

class BasketForm(forms.ModelForm):

    class Meta:
        model = BasketModel
        fields = ['quantity']


