from django.forms import ModelForm
from .models import Blog

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SIgnUpForm(UserCreationForm):

    class Meta:
        model=User
        fields= ('username', 'email', 'password1', 'password2')


class BlogForm(ModelForm):

    class Meta:
        model=Blog
        fields = "__all__"
        exclude = ("publish_date", "update_date")