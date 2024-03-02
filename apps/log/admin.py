from django.contrib import admin

from .models import ProfileViewLog


class ContentViewLogAdmin(admin.ModelAdmin):
    list_display = ("viewer", "viewed_profile", "viewed_at")
    list_filter = ("viewer", "viewed_profile")
    search_fields = ("viewer__username", "viewed_profile__id")
    date_hierarchy = "viewed_at"


admin.site.register(ProfileViewLog, ContentViewLogAdmin)
