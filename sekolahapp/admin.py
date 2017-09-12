# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sekolahapp.models import Jurusan, MataPelajaran
from userapp.models import Guru

# Register your models here.


class MataPelajaranInline(admin.TabularInline):
	model = MataPelajaran


class JurusanAdmin(admin.ModelAdmin):
	model = Jurusan
	inlines = [
		MataPelajaranInline,
	]


class GuruInline(admin.TabularInline):
	model = Guru


class MapelAdmin(admin.ModelAdmin):
	model = Jurusan
	inlines = [
		GuruInline,
	]

admin.site.register(Jurusan, JurusanAdmin)
admin.site.register(MataPelajaran, MapelAdmin)