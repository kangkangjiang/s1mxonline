# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 10:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgnization', '0002_courseorg_catgroy'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='syudent',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='catgroy',
            field=models.CharField(choices=[('gx', '高校'), ('gr', '个人'), ('pxjg', '培训机构')], default='pxjg', max_length=100, verbose_name='机构类别'),
        ),
    ]
