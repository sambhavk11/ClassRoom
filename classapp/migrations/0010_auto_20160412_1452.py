# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0009_auto_20160412_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]