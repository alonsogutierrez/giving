# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-27 01:19
from __future__ import unicode_literals

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttemptGift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, default=datetime.datetime(2017, 6, 27, 1, 19, 41, 942612))),
                (
                    'finish_date',
                    models.DateField(blank=True, default=datetime.datetime(2017, 6, 27, 1, 19, 41, 942669))),
                ('user_contacted', models.BooleanField(default=False)),
                ('received_gift', models.BooleanField(default=False)),
                ('process_finished', models.BooleanField(default=False)),
                ('aborted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryGift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=25, unique=True)),
                ('state_category', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2017, 6, 27, 1, 19, 41, 945786))),
                ('select', models.BooleanField(default=True)),
                ('num_likes', models.IntegerField(default=0)),
                ('num_dislikes', models.IntegerField(default=0)),
                ('state_comment', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComunaPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna_name', models.CharField(default=None, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='DispatchMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_type', models.CharField(default=None, max_length=35, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('length', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('cant_used_time', models.IntegerField(default=0)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                               to='obsequiemos.CategoryGift')),
            ],
        ),
        migrations.CreateModel(
            name='GiftDimensionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension_type', models.CharField(max_length=15, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GiftStateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_type', models.CharField(max_length=20, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GiftWeightType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_type', models.CharField(default=None, max_length=2, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50)),
                ('open', models.BooleanField(default=False)),
                ('url', models.URLField(default=None)),
                ('notified_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=b'post_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('detail', models.TextField(max_length=800)),
                ('state', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2017, 6, 27, 1, 19, 41, 940753))),
                (
                    'finish_date',
                    models.DateField(blank=True, default=datetime.datetime(2017, 6, 27, 1, 19, 41, 940809))),
                ('num_likes', models.IntegerField(default=0)),
                ('num_dislikes', models.IntegerField(default=0)),
                ('person2person_dispatch', models.BooleanField(default=False)),
                ('pay_winner_dispatch', models.BooleanField(default=False)),
                ('giver_pay_dispatch', models.BooleanField(default=False)),
                ('according_to_winner_dispatch', models.BooleanField(default=False)),
                ('comuna', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to='obsequiemos.ComunaPost')),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obsequiemos.Gift')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obsequiemos.Picture')),
            ],
        ),
        migrations.CreateModel(
            name='PostStateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_type', models.CharField(max_length=35, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postulations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(null=True)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2017, 6, 27, 1, 19, 41, 943992))),
                ('num_likes', models.IntegerField(default=0)),
                ('num_dislikes', models.IntegerField(default=0)),
                ('selected', models.BooleanField(default=False)),
                ('winner', models.BooleanField(default=False)),
                ('post_postulation',
                 models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='obsequiemos.Post')),
                ('user_postulation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                                       to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProvinciaPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia_name', models.CharField(default=b'', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='RegionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(default=None, max_length=50)),
                ('iso_3166_2_cl', models.CharField(default=None, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoryGift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subcategory', models.CharField(max_length=25, unique=True)),
                ('state_subcategory', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                               to='obsequiemos.CategoryGift')),
            ],
        ),
        migrations.CreateModel(
            name='UsedTimeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_type', models.CharField(max_length=15, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default=None, max_length=128, null=True)),
                ('phone', models.CharField(default=None, max_length=20, null=True)),
                ('avg_reputation', models.IntegerField(default=0, null=True)),
                ('picture', models.ImageField(default=None, upload_to=b'profile_images')),
                ('register_date', models.DateField(default=None, null=True)),
                ('cant_evaluaciones', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=25, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.UserType'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE,
                                       to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='provinciapost',
            name='region',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.RegionPost'),
        ),
        migrations.AddField(
            model_name='post',
            name='provincia',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.ProvinciaPost'),
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.RegionPost'),
        ),
        migrations.AddField(
            model_name='post',
            name='state_post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.PostStateType'),
        ),
        migrations.AddField(
            model_name='post',
            name='user_post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gift',
            name='dimension_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.GiftDimensionType'),
        ),
        migrations.AddField(
            model_name='gift',
            name='state_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.GiftStateType'),
        ),
        migrations.AddField(
            model_name='gift',
            name='subcategory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.SubcategoryGift'),
        ),
        migrations.AddField(
            model_name='gift',
            name='used_time_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.UsedTimeType'),
        ),
        migrations.AddField(
            model_name='gift',
            name='weight_type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.GiftWeightType'),
        ),
        migrations.AddField(
            model_name='comunapost',
            name='provincia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.ProvinciaPost'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='obsequiemos.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postulation_comment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='obsequiemos.Postulations'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attemptgift',
            name='post_attempt',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='obsequiemos.Post'),
        ),
    ]