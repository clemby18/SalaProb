
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('accounts.forms',
    url(r'^register/$', 'register'),
    url(r'^login/$', 'login_view'),
    url(r'^done/$', 'done'),
)

urlpatterns += patterns('rooms.views',
    #url(r'$', 'index'),
    url(r'^index/', 'index'),
    url(r'^opinions/(?P<id_category>\d+)', 'opinions'),
    url(r'^add_opinion/(?P<id>\d+)', 'add_opinion'),
)