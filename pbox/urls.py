from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include('pbox_backend.urls')),
)


urlpatterns += patterns('',
    url(r'^token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)