# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def default(request):
    """
    Render for the main page

    GET Links:
        -Sign In
        -User Dashboard
    """
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
    return HttpResponse('Sign in request process')

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
    return HttpResponse('Register request process')