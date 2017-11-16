# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..lr_app.models import Users

# Create your models here.
class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(Users, related_name='messages')

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Users, related_name='comments')
    message = models.ForeignKey(Messages,related_name='comments')