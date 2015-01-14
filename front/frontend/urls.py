from django.conf.urls import patterns, url

from frontend import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    # url(r'^info', views.info),   # Done
    # url(r'^user/me', views.user_me),
    # url(r'^user/(?P<id>\d+)/$', views.user_id),
    # url(r'^user/(?P<id>\d+)/(?P<pc_id>\d+)/$', views.pc_soft_list),


)
