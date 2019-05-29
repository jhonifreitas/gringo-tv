from django import forms

from gringo_tv.core import models


class ConfigForm(forms.ModelForm):

    class Meta:
        model = models.Config
        exclude = ['deleted_at']
