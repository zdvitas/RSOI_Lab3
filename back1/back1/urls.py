from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pcs.views.pc_list', name='home'),
    url(r'^one$', 'pcs.views.one', name='home'),
     # url(r'^blog/', include('blog.urls')),


)
