from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
