from django import forms
from django.contrib.auth.forms import AuthenticationForm

from gringo_tv.core import utils
from gringo_tv.custom_profile import models


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        exclude = ['user', 'points', 'deleted_at']

    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    username = forms.CharField(label="Usuário")
    phone = forms.CharField(label="Telefone")
    password = forms.CharField(label='Senha')
    password1 = forms.CharField(label='Confirme sua senha')

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
        profile = None
        if not self.initial.get('id'):
            data = self.cleaned_data.copy()
            data.pop('password1')
            data_user = {
                'first_name': data.pop('first_name'),
                'last_name': data.pop('last_name'),
                'username': data.pop('username'),
                'password': data.pop('password'),
            }
            user = models.User.objects.create_user(**data_user)
            profile = models.Profile.objects.create(user=user, **data)
        else:
            profile = super().save()

        if self.initial.get('id') and self.cleaned_data.get('password'):
            self.instance.user.set_password(self.cleaned_data.get('password'))

        return profile


class IndicationForm(forms.ModelForm):

    class Meta:
        model = models.Indication
        exclude = ['profile', 'status', 'deleted_at']

    phone = forms.CharField(label="Telefone")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = utils.Phone(phone).cleaning()
        return phone
