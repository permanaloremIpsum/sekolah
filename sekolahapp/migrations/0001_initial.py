# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, verbose_name='Jurusan')),
            ],
            options={
                'verbose_name_plural': 'Jurusan',
            },
        ),
        migrations.CreateModel(
            name='Mata_Pelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, verbose_name='Mata_Pelajaran')),
            ],
            options={
                'verbose_name_plural': 'Mata Pelajaran',
            },
        ),
    ]