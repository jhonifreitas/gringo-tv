from django import forms
from django.contrib.auth.forms import AuthenticationForm

from gringo_tv.core import utils
from gringo_tv.custom_profile import models


class LoginForm(AuthenticationForm):

    username = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))


class ProfileForm(forms.Form):

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nome'}), required=False)
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
                                required=False)
    username = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Usuário'}))
    phone = forms.CharField(label='', max_length=15,
                            widget=forms.TextInput(attrs={'placeholder': 'Telefone', 'type': 'tel'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = utils.Phone(phone).cleaning()
        return phone

    def clean(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if (password and password1) and (password != password1):
            self.add_error('password1', 'Senhas não são iguais!')
            raise forms.ValidationError('Senhas não são iguais!')

        return self.cleaned_data

    def save(self):
        data = self.cleaned_data.copy()
        data.pop('password1')
        data_user = {
            'first_name': data.pop('first_name'),
            'last_name': data.pop('last_name'),
            'username': data.pop('username'),
            'password': data.pop('password'),
        }
        user = models.User.objects.create_user(**data_user)
        return models.Profile.objects.create(user=user, **data)
