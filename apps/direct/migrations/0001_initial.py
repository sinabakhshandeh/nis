# Generated by Django 4.2 on 2024-03-02 16:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DirectChat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        related_name="direct_chats",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Participants",
                    ),
                ),
            ],
            options={
                "verbose_name": "Direct Chat",
                "verbose_name_plural": "Direct Chats",
            },
        ),
        migrations.CreateModel(
            name="DirectMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="Content")),
                (
                    "sent_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Sent At",
                    ),
                ),
                (
                    "chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="direct.directchat",
                        verbose_name="Chat",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Sender",
                    ),
                ),
            ],
            options={
                "verbose_name": "Direct Message",
                "verbose_name_plural": "Direct Messages",
                "ordering": ["sent_at"],
            },
        ),
    ]
