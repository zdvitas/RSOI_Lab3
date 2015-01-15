from django.conf.urls import patterns, url

from frontend import views, pc_view,soft_view

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^auth$', views.auth, name='home'),
    url(r'^logout', views.logout, name='home'),
    url(r'^pc$', pc_view.pc_list, name='home'),
    url(r'^pc/add$', pc_view.pc_add, name='home'),

    # url(r'^user/me', views.user_me),
    url(r'^pc/(?P<id>\d+)/$', pc_view.pc_one),
    url(r'^pc/delete/(?P<id>\d+)/$', pc_view.pc_delete),
    url(r'^pc/edit/(?P<id>\d+)/$', pc_view.pc_edit),

    url(r'^soft/add$', soft_view.soft_add, name='home'),
    url(r"^soft/(?P<id>\d+)/$", soft_view.soft_one),
    url(r'^soft/delete/(?P<id>\d+)/$', soft_view.soft_delete),
    url(r'^soft/edit/(?P<id>\d+)/$', soft_view.soft_edit),

    # url(r'^user/(?P<id>\d+)/(?P<pc_id>\d+)/$', views.pc_soft_list),


)
