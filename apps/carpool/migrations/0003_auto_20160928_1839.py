# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0002_remove_location_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
