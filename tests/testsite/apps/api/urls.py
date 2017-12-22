# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from testsite.apps.api.views import *

urlpatterns = [
    url(r'^automatic_error_str/$', automatic_error_str, name='automatic_error_str'),
    url(r'^automatic_error_json/$', automatic_error_json, name='automatic_error_json'),
    url(r'^first_name_str/$', first_name_str, name='first_name_str'),
    url(r'^first_and_last_name_str/$', first_and_last_name_str, name='first_and_last_name_str'),
    url(r'^last_name_str/$', last_name_str, name='last_name_str'),
    url(r'^email_str/$', email_str, name='email_str'),
    url(r'^email_json/$', email_json, name='email_json'),
]
