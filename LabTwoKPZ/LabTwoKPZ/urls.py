from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'labkpz.views.hello', name='main'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^action/$', 'labkpz.views.action'),
    url(r'^addapp/$', 'labkpz.views.addapp', name='addApp'),
    url(r'^addburn/$', 'labkpz.views.addburn', name='addBurn'),
    url(r'^addmarig/$', 'labkpz.views.addmarig', name='addMarig'),
    url(r'^adddie/$', 'labkpz.views.adddie', name='addDie'),
    url(r'^addchang/$', 'labkpz.views.addchang', name='addChang'),
    url(r'^addper/$', 'labkpz.views.addper', name='addPer'),
    url(r'^removeper/(?P<id>\d)$', 'labkpz.views.removeper'),
    url(r'^removeapp/(?P<id>\d)$', 'labkpz.views.removeapp'),
    url(r'^removemar/(?P<id>\d)$', 'labkpz.views.removemar'),
    url(r'^removeburn/(?P<id>\d)$', 'labkpz.views.removeburn'),
    url(r'^removedie/(?P<id>\d)$', 'labkpz.views.removedie'),
    url(r'^removechang/(?P<id>\d)$', 'labkpz.views.removechang'),
    url(r'^editper/(?P<id>\d)$', 'labkpz.views.editper'),
    url(r'^editapp/(?P<id>\d)$', 'labkpz.views.editapp'),
    url(r'^editmar/(?P<id>\d)$', 'labkpz.views.editmar'),
    url(r'^editdie/(?P<id>\d)$', 'labkpz.views.editdie'),
    url(r'^editburn/(?P<id>\d)$', 'labkpz.views.editburn'),
    url(r'^editchang/(?P<id>\d)$', 'labkpz.views.editchang')

)
