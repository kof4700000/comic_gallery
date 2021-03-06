# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Image(models.Model):
    volume = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    volume_name = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'

class Gallery(models.Model):
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    display_name = models.CharField(max_length=40, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    summary = models.CharField(max_length=300, blank=True, null=True)
    thumbnail = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery'

