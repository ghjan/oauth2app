from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^', include('mysite.apps.base.urls')),
    url(r'^account/', include('mysite.apps.account.urls')),
    url(r'^client/', include('mysite.apps.client.urls')),
    url(r'^oauth2/', include('mysite.apps.oauth2.urls')),
    url(r'^api/', include('mysite.apps.api.urls')),
]
