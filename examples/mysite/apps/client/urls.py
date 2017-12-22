#-*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from mysite.apps.client.views import client

urlpatterns = [
    url(r'^(?P<client_id>\w+)/?$', client, name='client'),

]
