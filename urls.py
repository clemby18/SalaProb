
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('aplikacja.views',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'index'),
    (r'^opinie/(?P<id_kategorii>\d+)', 'opinie'),
    (r'^index', 'index'),
    (r'^dodaj/(?P<id>\d+)', 'dodaj'),
    (r'^sukces', 'index'),
)
