# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-09 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('nova', '0025_appgroup_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetgroup',
            name='asset_groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='\u6240\u5c5e\u7528\u6237\u7ec4'),
        ),
    ]