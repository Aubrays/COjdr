# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0014_auto_20160627_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='race_picture',
            field=models.ImageField(blank=True, upload_to='races'),
        ),
    ]
