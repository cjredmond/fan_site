# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161010_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='rival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.House'),
        ),
    ]
