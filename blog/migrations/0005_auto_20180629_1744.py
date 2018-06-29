# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 08:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180629_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 8, 44, 31, 259950, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='address',
            name='numb',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='numb_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
