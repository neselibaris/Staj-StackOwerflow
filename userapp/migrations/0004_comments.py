# Generated by Django 4.2.3 on 2023-10-19 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userapp', '0003_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Açıklama')),
                ('createdAt', models.DateTimeField(auto_now=True, verbose_name='Oluşturma tarihi')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.post', verbose_name='Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazarı')),
            ],
        ),
    ]
