# Generated by Django 4.2 on 2024-03-02 16:57

import django.db.models.deletion
from django.db import migrations, models

import apps.direct.models.message


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("direct", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Media",
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
                    "file",
                    models.FileField(
                        upload_to=apps.direct.models.message.direct_message_upload_path
                    ),
                ),
                (
                    "file_type",
                    models.CharField(
                        choices=[
                            ("image", "IMAGE"),
                            ("video", "VIDEO"),
                            ("voice", "VOICE"),
                        ],
                        default="image",
                        help_text="Project current status",
                        max_length=25,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Text",
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
                ("text", models.CharField()),
            ],
        ),
        migrations.RemoveField(
            model_name="directmessage",
            name="content",
        ),
        migrations.CreateModel(
            name="DirectMessageContent",
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
                    "object_id",
                    models.PositiveIntegerField(verbose_name="Object ID"),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                        verbose_name="Content Type",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contents",
                        to="direct.directmessage",
                        verbose_name="Message",
                    ),
                ),
            ],
            options={
                "verbose_name": "Direct Message Content",
                "verbose_name_plural": "Direct Message Contents",
            },
        ),
    ]
