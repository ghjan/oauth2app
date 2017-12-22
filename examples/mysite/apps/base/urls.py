# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from mysite.apps.base.views import homepage

urlpatterns = [
    url(r'^/$', homepage, name='homepage'),
]
