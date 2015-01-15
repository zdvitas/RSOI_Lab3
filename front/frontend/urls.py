from django.conf.urls import patterns, url

from frontend import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^auth$', views.auth, name='home'),
    url(r'^pc$', views.pc_list, name='home'),
    url(r'^pc/add$', views.pc_add, name='home'),

    # url(r'^user/me', views.user_me),
    url(r'^pc/(?P<id>\d+)/$', views.pc_one),
    url(r'^pc/delete/(?P<id>\d+)/$', views.pc_delete),
    url(r'^pc/edit/(?P<id>\d+)/$', views.pc_edit),

    url(r'^soft/(?P<pc_id>\d+)/delete(?P<id>\d+)/$', views.soft_delete),
    url(r'^soft/(?P<pc_id>\d+)/edit(?P<id>\d+)/$', views.soft_edit),

    # url(r'^user/(?P<id>\d+)/(?P<pc_id>\d+)/$', views.pc_soft_list),


)
