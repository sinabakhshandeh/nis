from django.contrib import admin

from . import models


@admin.register(models.DirectChat)
class DirectChatAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
    filter_horizontal = ("participants",)
    search_fields = ["participants__username"]


@admin.register(models.DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "chat", "sent_at")
    list_filter = ["chat", "sender"]
    search_fields = ["sender__username", "content"]


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "file_type"]
    list_filter = ["file_type"]


@admin.register(models.Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


@admin.register(models.DirectMessageContent)
class DirectMessageContentAdmin(admin.ModelAdmin):
    list_display = ["id", "message", "content_type", "object_id"]
    list_filter = ["content_type"]
