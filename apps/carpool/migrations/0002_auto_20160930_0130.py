# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpool',
            name='arrival_time',
            field=models.TimeField(default="00:00:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carpool',
            name='num_passengers',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
