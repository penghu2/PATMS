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
from XTest.serializers import UserSerializer
import logging

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
    return render_to_response('index.html',
                            context_instance= RequestContext(request, processors=[custom_proc]))

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if username == '' or password == '':
        return render_to_response('login.html',
                  context_instance=RequestContext(request, processors=[custom_proc]))

    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("index")

    else:
        resp = HttpResponse()
        resp.write('username or password is wrong')
        return resp

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