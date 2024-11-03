# Generated by Django 5.1.1 on 2024-10-22 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [
                    ("block_users", "Может блокировать пользователей сервиса")
                ],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]