from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email','password1','password2','telefono','avatar']


class Proyecto(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ('modelo_coche', 'modelo_escape','modelo_llanta','modelo_volante','modelo_bk')



# class MarcaForm(forms.Form):
#     marca = forms.CharField(widget=forms.HiddenInput())