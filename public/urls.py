from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    ('^', include('todo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
