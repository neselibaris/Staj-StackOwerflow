# Generated by Django 4.2.3 on 2023-10-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0006_customuser_badgecount_customuser_followcount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badges',
            name='badgeGold',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='badgeSilver',
        ),
    ]
