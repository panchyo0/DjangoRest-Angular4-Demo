# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20180120_1740'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
