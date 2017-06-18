# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Article(models.Model):
  title = models.CharField(max_length=255)
  content = HTMLField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
  published = models.BooleanField(default=True)
  public_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-public_date']