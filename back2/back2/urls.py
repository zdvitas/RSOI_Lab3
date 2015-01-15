from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'back2.views.home', name='home'),
    url(r'^$', 'computers_app.views.soft_list', name='home'),
    url(r'^one$', 'computers_app.views.one', name='home'),
    # url(r'^blog/', include('blog.urls')),


)
