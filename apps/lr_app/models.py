# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt
# Create your models here.
class UsersManager(models.Manager):
    """
    Manages the server to databse queries for the Users table

    Attributes:
        addUser (data): adds singular user to the database
    """
    def addUser(self, data):
        """
        Add a user to the database
        Args:
            data (request.POST): post data from a form
        
        Returns:
            list: a list of responses from the manager, if any response is given; that data is rejected
        """
        response = []
        if not data['first_name']:
            response.append('Name field cannot be left empty!')
        elif not re.match(r'^[a-zA-Z ]+$', data['first_name']):
            response.append('First name can only contain alpha characters!')
        
        if not data['last_name']:
            response.append('Last name cannot be left empty!')
        elif not re.match(r'^[a-zA-Z ]+$', data['last_name']):
            response.append('Last name can only contain alpha characters!')

        if not data['email']:
            response.append('Email cannot be left empty!')
        elif not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', data['email']):
            response.append('Email entered is invalid!')
        elif len(Users.objects.filter(email=data['email'])) != 0:
            response.append('Email already exists!')
        
        if not data['password']:
            response.append('Password cannot be left empty!')
        elif not re.match(r'^[a-zA-Z0-9]+$', data['password']):
            response.append('Password can only contain aplha numeric characters!')
        elif data['password'] != data['confirm_password']:
            response.append('Passwords entered do not match!')
        
        if len(response) == 0:
            new_user = Users.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()),
                level = 0
            )
            if len(Users.objects.all()) == 1:
                new_user.level = 9
            else:
                new_user.level = 0
            new_user.save()
        return response


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    level = models.IntegerField()
    objects = UsersManager()