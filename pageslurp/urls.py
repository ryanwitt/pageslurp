from django.conf.urls.defaults import *
from pageslurp.page_receiver.views import receive
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^receive/.*', receive),
    (r'^admin/', include(admin.site.urls)),
)
