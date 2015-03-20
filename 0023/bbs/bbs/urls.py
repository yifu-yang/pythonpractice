from django.conf.urls import patterns, include, url
from django.contrib import admin
from bbs.view import hello,time,meta,bbs,addmessage,getmessagelist
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'hello/',hello),
	url(r"^time/plus/(\d{1,2})/$",time),
    url(r"^meta",meta),
    url(r"^bbs",bbs),
    url(r"^addmessage",addmessage),
    url(r"^getmessagelist",getmessagelist),
)
