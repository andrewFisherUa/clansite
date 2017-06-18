#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Category, Article
# import ipdb
import requests
from django.core import serializers
from phpserialize import *
from collections import OrderedDict
import json

class IndexView(ListView):
  model = Category
  template_name = 'clansite/index.html'
  context_object_name = 'news'
  def get_queryset(self):
    return Article.objects.filter(category=1)

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['category'] = Category.objects.get(pk=1)
    context['categories'] = Category.objects.order_by('id')
    return context

class CategoryView(ListView):
  model = Category
  template_name = 'clansite/category.html'
  context_object_name = 'articles'

  def get_queryset(self):
    return Article.objects.filter(category=self.kwargs['pk'])

  def get_context_data(self, **kwargs):
    context = super(CategoryView, self).get_context_data(**kwargs)
    context['category'] = Category.objects.get(pk=self.kwargs['pk'])
    context['categories'] = Category.objects.order_by('id')
    return context

class ClansView(TemplateView):
  template_name = 'clansite/clans.html'

  def get_context_data(self, **kwargs):
    context = super(ClansView, self).get_context_data(**kwargs)
    context['categories'] = Category.objects.order_by('id')
    clans = requests.get('http://api.neverfate.ru/clans.php')
    context['clans'] = loads(clans.text, object_hook=phpobject)
    print context['clans']
    return context

class ClanView(TemplateView):
  template_name = 'clansite/clan.html'

  def get_context_data(self, **kwargs):
    print self.kwargs['pk']
    context = super(ClanView, self).get_context_data(**kwargs)
    context['categories'] = Category.objects.order_by('id')
    url = 'http://api.neverfate.ru/sostav.php?cl=' + self.kwargs['pk']
    context['name'] = self.kwargs['pk']
    # print url
    clan = requests.get(url)
    # print clan.text
    context['clan'] = loads(clan.text, object_hook=phpobject)
    print context['clan']
    return context