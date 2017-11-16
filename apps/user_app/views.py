# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def add_new_user(request):
    """
    Renderer for adding a new user page

    GET Links:
        - Dashboard
        - Profile
        - Log off
    """
    return HttpResponse('add a new user page')

def add_new_user_p(request):
    """
    Route for processing a new user
    """
    return HttpResponse('process a new user')

def edit_user(request):
    """
    Renderer for editing their own info

    GET Links:
        - Dashboard
        - Profile
        - Log off
    """
    return HttpResponse('edit user info page')

def edit_user_p(request):
    """
    Route for processing a user edit request
    """
    return HttpResponse('edit self process')

def edit_user_by_id(request, u_id):
    """
    Renderer for editing a user by id

    GET Links:
        - Dashboard
        - Profile
        - Log off
    """
    return HttpResponse('edit user by id info page ' + str(u_id))

def edit_user_by_id_p(request, u_id):
    """
    Route for processing a user edit request by id
    """
    return HttpResponse('process user by id info page ' + str(u_id))

def show_user(request, u_id):
    """
    Renderer for showing a users page 
    
    GET Links:
        - Dashboard
        - Profile
        - Log off
        - To other users
    """
    return HttpResponse('User page ' + str(u_id))