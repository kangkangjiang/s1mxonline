# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20170810_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='课程标签'),
        ),
    ]
