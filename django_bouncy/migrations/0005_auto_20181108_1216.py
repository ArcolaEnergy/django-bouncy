# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bouncy', '0004_auto_20181106_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='processing_time',
            field=models.IntegerField(default=0),
        ),
    ]
