# Generated by Django 4.2.4 on 2023-10-11 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
