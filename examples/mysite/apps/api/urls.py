# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from mysite.apps.api.views import *

urlpatterns = [
    url(r'^date_joined/$', date_joined, name='date_joined'),
    url(r'^last_login/$', last_login, name='last_login'),
    url(r'^email/$', email, name='email'),
]
