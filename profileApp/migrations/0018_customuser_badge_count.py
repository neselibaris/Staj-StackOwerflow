# Generated by Django 4.2.7 on 2023-11-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0017_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='badge_count',
            field=models.IntegerField(default=0),
        ),
    ]
