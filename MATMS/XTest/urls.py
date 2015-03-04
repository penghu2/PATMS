__author__ = 'penghu2'

from django.conf.urls import patterns, url

urlpatterns = patterns('XTest.views',
                       url(r'^index.*','index', name='index'),

)