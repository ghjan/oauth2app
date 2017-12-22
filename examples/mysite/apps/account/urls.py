# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from mysite.apps.account.views import *

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', login, name='logout'),
    url(r'^signup/$', login, name='signup'),
    url(r'^clients/$', login, name='clients'),
]
