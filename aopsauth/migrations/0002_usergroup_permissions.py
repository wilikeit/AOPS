# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('aopsauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='\u7528\u6237\u7ec4\u6743\u9650'),
        ),
    ]
