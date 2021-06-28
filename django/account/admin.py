from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from reversion.admin import VersionAdmin


class AccountAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
    )
    search_fields = (
        "email",
        "username",
    )
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class SerieAdmin(VersionAdmin):
    list_display = ("readinglist", "tvshow", "id", "current_release_id", "release")
    search_fields = ("readinglist",)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ("readinglist",)
    fieldsets = ()


class ReadingListAdmin(VersionAdmin):
    list_display = ("account", "pk")
    search_fields = ("account", "pk")
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(ReadingList, ReadingListAdmin)
admin.site.register(Serie, SerieAdmin)
