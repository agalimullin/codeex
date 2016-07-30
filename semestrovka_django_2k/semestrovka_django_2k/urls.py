from django.conf.urls import include, url
from django.contrib import admin
from . import settings

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^auth/', include('client.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('goldenshop.urls', namespace="goldenshop")),
    url(r'^', include('catalog.urls', namespace="catalog")),
    url(r'^', include('cart.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
]
