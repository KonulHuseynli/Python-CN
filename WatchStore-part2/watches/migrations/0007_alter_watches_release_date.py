# Generated by Django 4.2 on 2024-12-10 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0006_watches_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watches',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 12, 10, 8, 17, 58, 221135, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
