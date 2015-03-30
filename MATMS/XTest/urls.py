__author__ = 'penghu2'

from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from XTest import views
from XTest.view import unitTestView




urlpatterns = patterns('XTest.views',
                       url(r'^index.*','index', name='index'),
                       url(r'^login.*','login', name='login'),
                       url(r'^logout.*','logout'),
                       url(r'^temp.*','temp'),

                       url(r'^deploy/.*', 'deploy'),

                     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += patterns('',
                        url(r'^UnitTest/detial/(?P<pk>[0-9]+)/$', unitTestView.UnitTestDetial.as_view()),
                        )

urlpatterns = format_suffix_patterns(urlpatterns)