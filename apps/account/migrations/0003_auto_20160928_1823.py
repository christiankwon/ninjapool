# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_carpool_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='carpool_id',
            field=models.IntegerField(null=True),
        ),
    ]
