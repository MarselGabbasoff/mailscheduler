# Generated by Django 5.1.1 on 2024-09-26 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_remove_client_avatar"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Distribution",
            new_name="Mailing",
        ),
        migrations.RenameModel(
            old_name="DistributionAttempt",
            new_name="MailingAttempt",
        ),
    ]