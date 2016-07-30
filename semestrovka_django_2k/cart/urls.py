from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^cart/$', 'cart.views.cart', name='cart'),
                       url(r'^del_from_cart/(?P<id>\d+)/$', 'cart.views.del_from_cart', name='del'),
                       url(r'^order/$', 'cart.views.order', name='order'),
                       url(r'^add_to_cart/(?P<id>\d+)/$', 'cart.views.add_to_cart', name='add_to_cart')
                       )
