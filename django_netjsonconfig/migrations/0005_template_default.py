# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 15:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0004_config_allow_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='default',
            field=models.BooleanField(db_index=True, default=False, help_text='whether new configurations will have this template enabled by default', verbose_name='enabled by default'),
        ),
    ]
