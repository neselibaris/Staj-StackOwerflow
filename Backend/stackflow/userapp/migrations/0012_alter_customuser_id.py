# Generated by Django 4.2.4 on 2023-10-11 14:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
