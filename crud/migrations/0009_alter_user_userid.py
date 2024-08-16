# Generated by Django 5.1 on 2024-08-14 09:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0008_alter_user_userid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="userId",
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True),
        ),
    ]
