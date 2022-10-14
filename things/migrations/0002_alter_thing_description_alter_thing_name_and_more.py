# Generated by Django 4.1.2 on 2022-10-14 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.TextField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
