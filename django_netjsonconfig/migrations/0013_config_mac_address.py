# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 10:17


import re

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0012_name_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='mac_address',
            field=models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', 32), code='invalid', message='Must be a valid mac address.')]),
        ),
    ]
