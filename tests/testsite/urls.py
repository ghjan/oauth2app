from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^oauth2/', include('testsite.apps.oauth2.urls')),
    url(r'^api/', include('testsite.apps.api.urls')),
    (r'^account/', include('testsite.apps.account.urls')),
]
