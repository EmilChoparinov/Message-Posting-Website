# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from ..lr_app.models import Users
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
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'dash_app/user.html', context)

def admin(request):
    """
    Renderer for admin dashboard
    """
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'dash_app/admin.html', context)

def determinePage(request):
    """
    Route for processing which page they will see
    """
    user = Users.objects.get(id=request.session['id'])
    if user.level == 9:
        return admin(request)
    else:
        return regular(request)