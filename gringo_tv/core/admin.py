from django.contrib import admin
from django.shortcuts import redirect

from gringo_tv.core import models


def redirect_one_object(model, obj):
    response = redirect(f'/admin/{model._meta.app_label}/{model._meta.model_name}/add/')
    if obj:
        response = redirect(f'/admin/{model._meta.app_label}/{model._meta.model_name}/{obj.pk}/change/')
    return response


@admin.register(models.Config)
class ConfigAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    change_form_template = "admin/button_save.html"

    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.first():
            return redirect_one_object(self.model, self.model.objects.first())
        return super().add_view(request, form_url='', extra_context=None)

    def changelist_view(self, request, extra_context=None):
        return redirect_one_object(self.model, self.model.objects.first())