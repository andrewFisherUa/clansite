from django.conf.urls import url

from . import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<pk>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^clans$', views.ClansView.as_view(), name='clans'),
    url(r'^clan/(?P<pk>[A-Za-z0-9.\s]+)$', views.ClanView.as_view(), name='clan')
]