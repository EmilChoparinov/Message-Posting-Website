# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..lr_app.models import Users

# Create your models here.
class MessagesManager(models.Manager):
    """
    Manages requests from the server and accordingly queries the database

    Attributes:
        addMessage: adds a message to the database
    """
    
    def addMessage(self, data, u_id):
        """
        Adds a message to the database

        Args:
            u_id (int): unique id of the user
            data (request.POST): request
        """
        response = []
        if not data['message']:
            response.append('Message cannot be empty!')
        if len(response) == 0:
            Users.objects.get(id=u_id).messages.add(
                Messages.objects.create(message=data['message'])
            )
        return response

class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(Users, related_name='messages')
    objects = MessagesManager()

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Users, related_name='comments')
    message = models.ForeignKey(Messages,related_name='comments')