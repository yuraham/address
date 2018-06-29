# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 07:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 7, 28, 36, 802249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
