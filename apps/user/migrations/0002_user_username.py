# Generated by Django 4.2 on 2024-03-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, null=True, unique=True),
        ),
    ]
