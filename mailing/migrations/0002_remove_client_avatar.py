# Generated by Django 5.1.1 on 2024-09-24 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="avatar",
        ),
    ]