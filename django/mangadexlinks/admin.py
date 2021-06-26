from django.contrib import admin
from .models import *


class MangaLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'uid')
    search_fields = ('title', 'uid')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class MangaGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid', 'language')
    search_fields = ('name', 'uid')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MangaLink, MangaLinkAdmin)
admin.site.register(MangaGroup, MangaGroupAdmin)
