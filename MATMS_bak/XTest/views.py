from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger('customapp.engine')


def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'STATIC_URL': settings.STATIC_URL
    }

#@login_required(login_url="/adminSys/login/")
def index(request):
    return render_to_response('index.html',
                            context_instance= RequestContext(request, processors=[custom_proc]))

