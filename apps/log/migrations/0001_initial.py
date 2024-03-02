# Generated by Django 4.2 on 2024-03-02 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileViewLog",
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
                    "viewed_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Viewed At",
                    ),
                ),
                (
                    "viewed_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_views",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Viewed Profile",
                    ),
                ),
                (
                    "viewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="viewed_profiles",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Viewer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile View Log",
                "verbose_name_plural": "Profile View Logs",
            },
        ),
    ]