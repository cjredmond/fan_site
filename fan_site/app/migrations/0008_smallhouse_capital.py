# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161011_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='smallhouse',
            name='capital',
            field=models.CharField(default='a', max_length=45),
        ),
    ]