# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CzlonekRodziny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=128)),
                ('nazwisko', models.CharField(max_length=128)),
                ('wiek', models.IntegerField()),
            ],
        ),
    ]