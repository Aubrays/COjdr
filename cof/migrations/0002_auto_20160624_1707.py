# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perso',
            name='age',
            field=models.PositiveSmallIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='perso',
            name='charisma',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perso',
            name='constitution',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perso',
            name='dexterity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perso',
            name='height',
            field=models.PositiveSmallIntegerField(default=80),
        ),
        migrations.AddField(
            model_name='perso',
            name='intelligence',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perso',
            name='level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='perso',
            name='strength',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perso',
            name='weight',
            field=models.PositiveSmallIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='perso',
            name='wisdom',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='hit_dice',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='race_description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='trait_charisma',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='race',
            name='trait_constitution',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='race',
            name='trait_dexterity',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='race',
            name='trait_intelligence',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='race',
            name='trait_strength',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='race',
            name='trait_wisdom',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='racetrait',
            name='trait_description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]
