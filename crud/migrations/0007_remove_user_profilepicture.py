# Generated by Django 5.1 on 2024-08-14 09:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0006_alter_user_profilepicture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profilePicture",
        ),
    ]
