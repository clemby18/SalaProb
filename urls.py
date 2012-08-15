
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('aplikacja.views',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'index'),
    (r'^opinions/(?P<id_Category>\d+)', 'opinions'),
    (r'^index', 'index'),
    (r'^addOpinions/(?P<id>\d+)', 'addOpinion'),
    (r'^success', 'index'),
)
