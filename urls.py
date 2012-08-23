
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('aplikacja.views',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'index'),
    (r'^opinions/(?P<id_category>\d+)', 'opinions'),
    (r'^index/', 'index'),
    (r'^add_opinion/(?P<id>\d+)', 'add_opinion'),
    (r'^success/', 'success'),
    (r'^registration/', 'registration'),
    (r'^login/', 'my_login'),
    (r'^invalid_login/', 'invalid_login'),
    (r'^inactive_account/', 'inactive_account'),
    (r'^logout/', 'my_logout'),
)
