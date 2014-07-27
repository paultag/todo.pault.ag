from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^voice/', 'todo.views.voice'),
    url(r'^text/', 'todo.views.text'),
)
