# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 20:32
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('clansite', '0002_auto_20170616_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
