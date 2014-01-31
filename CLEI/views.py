from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def login_user(request):
    logout(request)
    username = password = ''
    admin = False
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
       	    login(request, user)
            return render_to_response('home.html', context_instance=RequestContext(request))

    return render_to_response('login.html', context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))
