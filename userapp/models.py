# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SEX_CHOICES = (
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
)

KELAS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

# Create your models here.
class Guru(models.Model):
    nip = models.CharField('NIP', max_length=10, unique=True)
    nama = models.CharField('Nama', max_length=100, null=True)
    mapel = models.ForeignKey('sekolahapp.MataPelajaran', blank=True, null=True)

    def __unicode__(self):
        return '%s-%s' % (self.nip, self.nama)

    class Meta:
        verbose_name_plural = 'Guru'


class Siswa(models.Model):
    nis = models.CharField('NIS', max_length=10, unique=True)
    nama = models.CharField('Nama', max_length=100, null=True)
    tanggal_lahir = models.DateField(
        'Tanggal Lahir', help_text='Format Tanggal: YYYY-MM-DD')
    jenis_kelamin = models.CharField(
        'Jenis Kelamin',
        max_length=10,
        choices=SEX_CHOICES,
        default='Laki-laki')
    alamat = models.TextField('Alamat', blank=True, null=True)
    kelas = models.CharField(
        'Kelas',
        max_length=1,
        choices=KELAS_CHOICES,
        default='1')
    jurusan = models.ForeignKey('sekolahapp.Jurusan', null=True)
    mapel = models.ManyToManyField('sekolahapp.MataPelajaran')

    def __unicode__(self):
        return '%s-%s' % (self.nis, self.nama)

    class Meta:
        verbose_name_plural = 'Siswa'