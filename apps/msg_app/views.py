# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def add_message(request, u_id):
    """
    Route for processing a message into a user
    """
    return HttpResponse('add a message for ' + str(u_id))

def post_comment(request, u_id, m_id):
    """
    Route for processing a comment for a message on a user
    """
    return HttpResponse('add a comment on message ' + str(m_id) + " for user " + str(u_id))