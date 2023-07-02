from django import forms

from .models import Post, Menu, Attracs

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('price', 'dish')


class KidsForm(forms.ModelForm):
    class Meta:
        model = Attracs
        fields = ('price', 'name', 'image')





