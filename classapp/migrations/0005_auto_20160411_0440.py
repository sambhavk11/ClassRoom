# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 04:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0004_auto_20160410_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modules',
            old_name='student_id',
            new_name='student',
        ),
    ]
