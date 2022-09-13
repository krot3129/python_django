from django import forms
from .models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
    # name = forms.CharField(label='Заголовок')
    # content = forms.CharField(widget = forms.Textarea(attrs={'cols':60, 'rows':10 }), label='Содержание новости')
    # active = forms.BooleanField(label='Статус')



class CommentForm(forms.Form):
    # class Meta:
    #     model = Comment
    #     fields = '__all__'
     name = forms.CharField(label='Заголовок комментария')
     body = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label='Комментарий')