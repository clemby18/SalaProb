
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += patterns('accounts.forms',
    url(r'^register/$', 'register'),
    url(r'^login/$', 'login_view'),
    url(r'^logout/$', 'logout_view'),
    url(r'^done/$', 'done'),
    url(r'^welcome/$', 'welcome'),
    url(r'^users/$', 'users'),
)

urlpatterns += patterns('rooms.views',
    #url(r'$', 'index'),
    url(r'^index/', 'index'),
    url(r'^opinions/(?P<id_category>\d+)', 'opinions'),
    url(r'^add_opinion/(?P<id>\d+)', 'add_opinion'),
    url(r'^c_add_opinion/(?P<id>\d+)', 'c_add_opinion'),
    url(r'^some', 'some_view'),
)