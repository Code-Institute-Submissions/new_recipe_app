# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 19:01
from __future__ import unicode_literals

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171007_1952'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.AccountUserManager()),
            ],
        ),
    ]
