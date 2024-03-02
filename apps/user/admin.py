from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    model = models.User  # type: ignore
    ordering = ("email",)
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
        "is_staff",
        "is_superuser",
    )
    readonly_fields = ("uuid",)
    fieldsets = (  # type: ignore
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "username", "uuid")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
