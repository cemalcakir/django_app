from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Post, Comment


class CreateViewModelForm(forms.ModelForm):
    title = forms.CharField(label=_("Başlık"))
    content = forms.CharField(label="Sorunuz", widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="El Cevap", widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ("body", )
