# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 07:23
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('numb', models.IntegerField(max_length=10)),
                ('numb_num', models.IntegerField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 6, 29, 7, 23, 3, 746163, tzinfo=utc))),
                ('open_addr', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
