# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-22 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salt_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salt',
            name='name',
            field=models.CharField(db_index=True, max_length=250, unique=True),
        ),
    ]
