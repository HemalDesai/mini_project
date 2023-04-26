from django import forms
from .models import *


class LNFProductForm(forms.ModelForm):

    class Meta:
        model = LNFProducts
        fields = "__all__"
        exclude = ['username', 'color']
