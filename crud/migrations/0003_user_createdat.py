# Generated by Django 5.1 on 2024-08-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0002_rename_userid_user_userid"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="createdAt",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
