# Generated by Django 4.2.4 on 2023-10-16 12:28

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagler', models.CharField(max_length=10, verbose_name='Tagler')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Başlık')),
                ('description', models.TextField(max_length=500, null=True, verbose_name='Açıklama')),
                ('createdAt', models.DateTimeField(auto_now=True, verbose_name='Oluşturma tarihi')),
                ('viewed', models.IntegerField(default=0, verbose_name='Görüntülenme Sayısı')),
                ('like', models.IntegerField(default=0, verbose_name='Beğeni Sayısı')),
                ('comment', models.IntegerField(default=0, verbose_name='Yorum Sayısı')),
                ('kodalanı', ckeditor.fields.RichTextField(max_length=1500, null=True, verbose_name='Kod Bloğu')),
                ('tagleri', models.ManyToManyField(related_name='Tagleri', to='userapp.tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazarı')),
            ],
        ),
    ]