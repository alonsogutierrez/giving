# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-29 00:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obsequiemos', '0003_merge_20170829_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attemptgift',
            name='finish_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 29, 0, 6, 13, 483250)),
        ),
        migrations.AlterField(
            model_name='attemptgift',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 29, 0, 6, 13, 483186)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 29, 0, 6, 13, 489320)),
        ),
        migrations.AlterField(
            model_name='gift',
            name='name',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'post_pictures'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 29, 0, 6, 13, 480825)),
        ),
        migrations.AlterField(
            model_name='post',
            name='finish_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 29, 0, 6, 13, 480897)),
        ),
        migrations.AlterField(
            model_name='postulations',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 8, 29, 0, 6, 13, 486275)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=b'profile_images'),
        ),
    ]
