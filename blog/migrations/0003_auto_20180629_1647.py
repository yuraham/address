# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 07:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180629_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 7, 47, 6, 52358, tzinfo=utc)),
        ),
    ]