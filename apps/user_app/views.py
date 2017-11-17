# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

from ..lr_app.models import Users
# Create your views here.
def add_new_user(request):
    """
    Renderer for adding a new user page

    GET Links:
        - Dashboard
        - Profile
        - Log off
    """
    admin = Users.objects.get(id=request.session['id'])
    if admin.level == 9:
        return render(request, 'user_app/new.html')
    return redirect('/dashboard')

def add_new_user_p(request):
    """
    Route for processing a new user
    """
    if request.method == 'POST':
        response = Users.objects.addUser(request.POST)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/users/new')
    return redirect('/dashboard')

def edit_user(request):
    """
    Renderer for editing their own info

    GET Links:
        - Dashboard
        - Profile
        - Log off
    """
    return render(request, 'user_app/self_edit.html')

def edit_user_p(request):
    """
    Route for processing a user edit request
    """
    if request.method == 'POST':    
        response = Users.objects.change(request.POST, request.session['id'])
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/users/edit')
    return redirect('/users/show/' + str(request.session['id']))

def edit_user_by_id(request, u_id):
    """
    Renderer for editing a user by id

    GET Links:
        - Dashboard
        - Profile
        - Log off
    """
    return render(request, 'user_app/admin_edit.html', {'user_id': u_id})

def edit_user_by_id_p(request, u_id):
    """
    Route for processing a user edit request by id
    """
    if request.method == 'POST':    
        response = Users.objects.change(request.POST, u_id)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/users/edit/' + str(u_id))
    return redirect('/dashboard')

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