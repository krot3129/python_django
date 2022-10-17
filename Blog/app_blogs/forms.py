from django import forms
from .models import BlogModel, Image, Profile
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content']

class ImageForm(forms.ModelForm):

    image = forms.ImageField(label='image')
    class Meta:
        model = Image
        fields = ['image']


class UploadcvsForm(forms.Form):
    file = forms.FileField()



class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','about', 'email', 'city', 'avatar']
