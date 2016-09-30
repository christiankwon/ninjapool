# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_merge_20160929_1811'),
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
        ),
        migrations.AlterField(
            model_name='wall',
            name='users',
            field=models.ManyToManyField(related_name='messages', to='account.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='walls',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wall.Wall'),
        ),
    ]
