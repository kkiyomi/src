from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin


class TVShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'date_added', 'state')
    search_fields = ('title',)
    readonly_fields = ('date_added',)

    filter_horizontal = ('genre', 'cast')
    list_filter = ('state',)
    fieldsets = ()
    actions = [
        'make_published',
        'make_pending',
        'make_archive',
        'make_delete',
    ]

    def make_published(self, request, queryset):
        queryset.update(state='Published')
    make_published.short_description = "Mark as Published"

    def make_pending(self, request, queryset):
        queryset.update(state='Pending')
    make_pending.short_description = "Mark as Pending"

    def make_archive(self, request, queryset):
        queryset.update(state='Archived')
    make_archive.short_description = "Mark as Archived"

    def make_delete(self, request, queryset):
        queryset.update(state='Deleted')
    make_delete.short_description = "Mark as Deleted"


class ReleaseV2Admin(admin.ModelAdmin):
    list_display = ('number', 'tvshow', 'date_added')
    search_fields = ('tvshow',)
    readonly_fields = ('date_added',)

    filter_horizontal = ()
    list_filter = ('tvshow',)
    fieldsets = ()


class ReleaseV2Admin2(VersionAdmin):
    list_display = ('date_added', 'number', 'tvshow')
    search_fields = ('tvshow',)
    readonly_fields = ('date_added',)

    filter_horizontal = ()
    list_filter = ('tvshow',)
    fieldsets = ()


admin.site.register(TVShow, TVShowAdmin)
admin.site.register(ReleaseV2, ReleaseV2Admin2)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Network)
admin.site.register(Country)
