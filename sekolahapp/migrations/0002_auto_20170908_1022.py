# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolahapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Mata Pelajaran',
            },
        ),
        migrations.DeleteModel(
            name='Mata_Pelajaran',
        ),
        migrations.AddField(
            model_name='jurusan',
            name='kode',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='jurusan',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matapelajaran',
            name='jurusan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolahapp.Jurusan'),
        ),
    ]
