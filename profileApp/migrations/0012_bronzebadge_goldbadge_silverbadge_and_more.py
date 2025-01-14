# Generated by Django 4.2.3 on 2023-10-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0011_remove_badges_user_customuser_badge'),
    ]

    operations = [
        migrations.CreateModel(
            name='bronzeBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bronzeTitle', models.CharField(default='Bronze Badge Title', max_length=50)),
                ('bronzeAciklama', models.TextField(blank=True, default='Bronze Badge Description')),
                ('badgeBronze', models.ImageField(blank=True, default='./badges/badge_bronze.jpg', null=True, upload_to='badges/')),
            ],
            options={
                'verbose_name': 'bronzeBadge',
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.CreateModel(
            name='goldBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goldTitle', models.CharField(default='gold Badge Title', max_length=50)),
                ('goldAciklama', models.TextField(blank=True, default='gold Badge Description')),
                ('badgeGold', models.ImageField(blank=True, default='./badges/badge_gold.jpg', null=True, upload_to='badges/')),
            ],
            options={
                'verbose_name': 'goldBadge',
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.CreateModel(
            name='silverBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silverTitle', models.CharField(default='Silver Badge Title', max_length=50)),
                ('silverAciklama', models.TextField(blank=True, default='Silver Badge Description')),
                ('badgeSilver', models.ImageField(blank=True, default='./badges/badge_silver.jpg', null=True, upload_to='badges/')),
            ],
            options={
                'verbose_name': 'silverBadge',
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.AlterModelOptions(
            name='badges',
            options={},
        ),
        migrations.RemoveField(
            model_name='badges',
            name='badgeBronze',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='badgeGold',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='badgeSilver',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='bronzeAciklama',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='bronzeTitle',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='goldAciklama',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='goldTitle',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='silverAciklama',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='silverTitle',
        ),
    ]
