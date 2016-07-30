from django.conf.urls import url, patterns

urlpatterns = patterns('',
                       url(r'^$', 'goldenshop.views.index'),
                       url(r"^page/(\d+)/$", 'goldenshop.views.index'),
                       url(r'^about', 'goldenshop.views.about', name='about'),
                       url(r'^contact', 'goldenshop.views.contact', name='contact'),
                       url(r'^reviews', 'goldenshop.views.review', name='reviews'),
                       url(r'^add_reviews', 'goldenshop.views.add_review', name='add_reviews')
                       )
