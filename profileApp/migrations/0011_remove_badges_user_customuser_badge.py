# Generated by Django 4.2.3 on 2023-10-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0010_alter_badges_badgebronze_alter_badges_badgegold_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badges',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='badge',
            field=models.ManyToManyField(related_name='Badges', to='profileApp.badges'),
        ),
    ]
