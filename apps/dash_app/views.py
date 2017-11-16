# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def regular(request):
    """
    Renderer for user dashboard

    GET Links:
        - Users/id
        - User Profile
        - New users
        - Log off
    """
    return HttpResponse('Dashboard page')

def admin(request):
    """
    Renderer for admin dashboard
    """
    return HttpResponse('Admin page')

def determinePage(request):
    """
    Route for processing which page they will see
    """
    return HttpResponse('Admin or User check')