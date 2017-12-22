# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from oauth2app.token import handler, TokenGenerator
from testsite.apps.oauth2.views import *

urlpatterns = [
    url(r'^missing_redirect_uri/$', missing_redirect_uri, name='missing_redirect_uri'),
    url(r'^token/$', handler, name='token.handler'),
    url(r'^token_mac/$', TokenGenerator(authentication_method=MAC), name='token_mac'),
    url(r'^authorize_not_refreshable/$', authorize_not_refreshable, name='authorize_not_refreshable'),
    url(r'^authorize_mac/$', authorize_mac, name='authorize_mac'),
    url(r'^authorize_first_name/$', authorize_first_name, name='authorize_first_name'),
    url(r'^authorize_last_name/$', authorize_last_name, name='authorize_last_name'),
    url(r'^authorize_first_and_last_name/$', authorize_first_and_last_name, name='authorize_first_and_last_name'),
    url(r'^authorize_no_scope/$', authorize_no_scope, name='authorize_no_scope'),
    url(r'^authorize_code/$', authorize_code, name='authorize_code'),
    url(r'^authorize_token/$', authorize_token, name='authorize_token'),
    url(r'^authorize_token_mac/$', authorize_token_mac, name='authorize_token_mac'),
    url(r'^authorize_code_and_token/$', authorize_code_and_token, name='authorize_code_and_token'),
]
