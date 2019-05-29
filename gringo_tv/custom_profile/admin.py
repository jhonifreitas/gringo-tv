from django.contrib import admin

from gringo_tv.custom_profile import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['id', 'user', 'phone', 'points', 'updated_at', 'created_at']
    list_display_links = ['id', 'user']


@admin.register(models.Indication)
class IndicationAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['id', 'profile', 'phone', 'status', 'updated_at', 'created_at']
    list_display_links = ['id', 'profile']
