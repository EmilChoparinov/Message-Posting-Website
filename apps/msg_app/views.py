# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect

from ..lr_app.models import Users
from models import Messages, Comments
from django.contrib import messages
# Create your views here.
def add_message(request, u_id):
    """
    Route for processing a message into a user
    """
    if request.method == 'POST':
        response = Messages.objects.addMessage(request.POST, u_id)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
    return redirect('/users/show/'+str(u_id))

def post_comment(request, u_id, m_id):
    """
    Route for processing a comment for a message on a user
    """
    return HttpResponse('add a comment on message ' + str(m_id) + " for user " + str(u_id))