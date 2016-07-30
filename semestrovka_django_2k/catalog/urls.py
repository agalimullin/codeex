from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^categories/(?P<id>\d+)/$', 'catalog.views.one_category', name='by_category'),
                       url(r'^product/(?P<id>\d+)/$', 'catalog.views.product', name='product'),
                       url(r"^products/add_like/(?P<id>\d+)/$", 'catalog.views.add_like_product',
                           name='add_like_product'),
                       url(r'^add_comment/(?P<id>\d+)/$', 'catalog.views.add_comment', name='add_comment'),
                       url(r'^del_comment/(?P<id>\d+)/$', 'catalog.views.del_comment', name='del_comment'),
                       url(r'^search/$', 'catalog.views.search', name='search'),
                       )
