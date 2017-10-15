# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 01:33
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0015_auto_20170828_1649'),
        ('operation', '0006_auto_20170810_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='courses.Courses', verbose_name='课程名')),
                ('user', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名字')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
            },
        ),
    ]