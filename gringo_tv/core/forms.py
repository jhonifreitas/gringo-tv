from django import forms

from gringo_tv.core import models


class ConfigForm(forms.ModelForm):

    class Meta:
        model = models.Config
        exclude = ['deleted_at']

    datetime = forms.DateTimeField(label='Data/Hora')

    def clean_datetime(self):
        datetime = self.cleaned_data.get('datetime')
        print(datetime)
        return datetime
