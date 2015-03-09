__author__ = 'penghu2'

from django.conf.urls import patterns, url, include
from rest_framework import routers
from XTest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('XTest.views',
                       url(r'^index.*','index', name='index'),
                       url(r'^login.*','login', name='login'),
                       url(r'^logout.*','logout'),
                       url(r'^temp.*','temp'),
                       url(r'^', include(router.urls)),
                     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)