# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Users
from django.contrib import messages
# Create your views here.
def default(request):
    """
    Render for the main page

    GET Links:
        -Sign In
        -User Dashboard
    """
    if 'id' in request.session:
        return redirect('/dashboard')
    return render(request, 'lr_app/default.html')

def signin(request):
    """
    Renderer for the sign in page
    
    GET Links:
        - User Dashboard
        - Register
    """
    return render(request, 'lr_app/signin.html')

def signin_p(request):
    """
    Route for processing sign in request
    """
    if request.method == 'POST':
        response = Users.objects.login(request.POST)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/signin')
        request.session['id'] = Users.objects.get(email=request.POST['email']).id
        return redirect('/dashboard')
    return redirect(request, '/')

def register(request):
    """
    Renderer for the register page

    GET Links:
        - Sign In
        - User Dashboard
    """
    return render(request, 'lr_app/register.html')

def register_p(request):
    """
    Route for processing register request
    """
    if request.method == 'POST':
        response = Users.objects.addUser(request.POST)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/register')
        return redirect('/dashboard')
    return redirect('/')

def signout(request):
    """
    Route for processing a logout request
    """
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/')