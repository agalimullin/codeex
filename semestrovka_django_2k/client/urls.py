from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin', admin.site.urls),
                       url(r'^profile', 'client.views.user_profile', name='profile'),
                       url(r'^changeimage', 'client.views.refresh_image', name='changeimage'),
                       url(r'^login', 'client.views.login', name='login'),
                       url(r'^logout', 'client.views.logout', name='logout'),
                       url(r'^registration', 'client.views.registration', name='registration')
                       )
