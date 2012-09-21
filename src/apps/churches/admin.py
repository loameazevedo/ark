# -*- coding: utf8 -*-

from django.contrib import admin

from src.apps.churches.models import Church


class ChurchAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'email', 'phone', 'members')

admin.site.register(Church, ChurchAdmin)
