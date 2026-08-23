from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ClientUser


@admin.register(ClientUser)
class ClientUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Client profile", {
            "fields": ("age", "location", "phone", "balance"),
        }),
    )