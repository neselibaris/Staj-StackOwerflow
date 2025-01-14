# Generated by Django 4.2.3 on 2023-10-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0009_alter_badges_options_remove_badges_aciklama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badges',
            name='badgeBronze',
            field=models.ImageField(blank=True, default='./badges/badge_bronze.jpg', null=True, upload_to='badges/'),
        ),
        migrations.AlterField(
            model_name='badges',
            name='badgeGold',
            field=models.ImageField(blank=True, default='./badges/badge_gold.jpg', null=True, upload_to='badges/'),
        ),
        migrations.AlterField(
            model_name='badges',
            name='badgeSilver',
            field=models.ImageField(blank=True, default='./badges/badge_silver.jpg', null=True, upload_to='badges/'),
        ),
    ]
