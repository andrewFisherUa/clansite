# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

from .models import Category, Article

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
