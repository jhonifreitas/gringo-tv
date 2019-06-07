from django.contrib import admin

from gringo_tv.dealer import models


@admin.register(models.Dealer)
class DealerAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['id', 'user', 'phone', 'updated_at', 'created_at']
    list_display_links = ['id', 'user']
