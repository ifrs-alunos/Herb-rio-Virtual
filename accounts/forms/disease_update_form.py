from django import forms
from django.forms import widgets

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(label="E-mail")

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = "Credencial utilizada para login. Use letras, números e os símbolos @/./+/-/_ apenas."


    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Nome de usuário',
        }