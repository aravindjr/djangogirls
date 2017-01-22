# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 09:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 22, 9, 51, 20, 628973, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]