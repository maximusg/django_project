# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20171030_1558'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Treasure2',
            new_name='Treasure',
        ),
    ]