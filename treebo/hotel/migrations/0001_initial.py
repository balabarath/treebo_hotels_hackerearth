# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-01 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.TextField()),
                ('rating', models.FloatField()),
                ('link', models.TextField()),
                ('actual_price', models.FloatField()),
                ('discount', models.IntegerField()),
                ('location', models.TextField()),
            ],
        ),
    ]
