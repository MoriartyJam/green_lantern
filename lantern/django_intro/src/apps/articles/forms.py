from django import forms

from apps.articles.models import Article


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleImageForm(forms.Form):
    image = forms.ImageField(required=False)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'tags', 'author', 'image']