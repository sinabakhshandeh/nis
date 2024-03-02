from django.contrib import admin

from .models import DirectChat, DirectMessage


class DirectChatAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
    filter_horizontal = ("participants",)
    search_fields = ["participants__username"]


class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "chat", "sent_at")
    list_filter = ("chat",)
    search_fields = ["sender__username", "content"]


admin.site.register(DirectChat, DirectChatAdmin)
admin.site.register(DirectMessage, DirectMessageAdmin)
