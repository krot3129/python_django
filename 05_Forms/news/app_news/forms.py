from django import forms
# from .models import News, Comment


class NewsForm(forms.Form):
    name = forms.CharField(label='Заголовок')
    content = forms.CharField(widget = forms.Textarea(attrs={'cols':60, 'rows':10 }), label='Содержание новости')
    active = forms.BooleanField(label='Статус')


class CommentForm(forms.Form):
     name = forms.CharField(label='Заголовок')
     body = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label='Комментарий')