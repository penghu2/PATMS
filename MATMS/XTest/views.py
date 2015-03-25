#encoding=utf-8
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from XTest.serializers import UserSerializer
import logging
from commons import JSONResponse

logger = logging.getLogger('customapp.engine')

def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'STATIC_URL': settings.STATIC_URL
    }

@login_required(login_url="/ATMS/login/")
def index(request):
    return render_to_response('unittest.html',{'menuName':'测试管理', 'UserName':request.user.username},
                            context_instance= RequestContext(request, processors=[custom_proc]))

def temp(request):
    return render_to_response('base.html',{'menuName':'测试管理'},
                            context_instance= RequestContext(request, processors=[custom_proc]))

@api_view(http_method_names=['POST','GET'])
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    next = request.GET.get('next',None)
    if username == '' or password == '':
        return render_to_response('login.html',
                  context_instance=RequestContext(request, processors=[custom_proc]))
    print username, password
    user = auth.authenticate(username=username, password=password)
    resp={}
    if user is not None and user.is_active:
        auth.login(request, user)
        #return HttpResponseRedirect("index")

        resp['status'] = '0000'
        if next is None:
            next = '/ATMS/index'
        resp['href']=next
        return JSONResponse(resp)

    else:
        resp['status'] = '1001'
        resp['href']='/ATMS/index'
        return JSONResponse(resp)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("login")


def regist(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')

    user = User.objects.create_user(username, email, password)
    user.save()

class UserViewSet(viewsets.ModelViewSet):
    """
    allowed to view and user model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer