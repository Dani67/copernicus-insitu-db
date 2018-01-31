# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-31 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insitu', '0017_rename_coverage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='copernicusservice',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='entrustedentity',
            name='acronym',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
