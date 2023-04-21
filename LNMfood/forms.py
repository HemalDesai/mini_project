from django import forms
from .models import *


class BlogfoodForm(forms.ModelForm):

    class Meta_food:
        model = Blog_food
        fields = '__all__'
        exclude = ['username']