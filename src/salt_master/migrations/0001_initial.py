# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 07:01
from __future__ import unicode_literals

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
            name='Salt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('use_time', models.TimeField(blank=True, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Salt',
                'verbose_name_plural': 'Salts',
            },
        ),
    ]
