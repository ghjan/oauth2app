# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from oauth2app.token import handler, TokenGenerator
from mysite.apps.oauth2.views import *

urlpatterns = [
    url(r'^missing_redirect_uri/$', missing_redirect_uri, name='missing_redirect_uri'),
    url(r'^authorize/$', authorize, name='missing_redirect_uri'),
    url(r'^token/$', handler, name='token.handler'),
]
