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
            list: a list of responses from the manager, if any response is given; the request is rejected
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

    def login(self, data):
        """
        Checks with the database if its okay to log this user into the requested account

        Args:
            data (request.POST): post data from a form
        
        Returns:
            list: a list of responses from the manager, if any response is given; the request is rejected
        """
        response = []
        if not data['email']:
            response.append('Email cannot be left blank!')
        elif len(Users.objects.filter(email=data['email'])) == 0:
            response.append('Email is not registered!')
        elif not bcrypt.checkpw(data['password'].encode(), Users.objects.get(email=data['email']).password.encode()):
            response.append('Password is not correct!')
        if not data['password']:
            response.append('Password cannot be left blank!')
        return response

    def change(self, data, u_id):
        """
        Changes a users data that is currently inside the database

        Args:
            data (request.POST): post data from a form
            u_id (int): user's unique id
        
        Returns:
            list: a list of responses from the manager, if any response is given; the request is rejected
        """
        response = []
        user = Users.objects.get(id=u_id)
        if data['type'] == 'info':
            if data['first_name']:
                if not re.match(r'^[a-zA-Z ]+$', data['first_name']):
                    response.append('First name can only contain alpha characters!')
                else:
                    user.first_name = data['first_name']
            
            if data['last_name']:
                if not re.match(r'^[a-zA-Z ]+$', data['last_name']):
                    response.append('Last name can only contain alpha characters!')
                else:
                    user.last_name = data['last_name']

            if data['email']:
                if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', data['email']):
                    response.append('Email entered is invalid!')
                elif Users.objects.filter(email=data['email']) < 1:
                    if Users.objects.filter(email=data['email'])[0] != Users.objects.get(id=u_id).email:
                        response.append('Email is already linked to another account!')
                else:
                    user.email = data['email']
            if 'level' in data:
                print "*"*50
                print data['level']
                user.level = int(data['level'])

        elif data['type'] == 'password':
            if not data['password']:
                response.append('Password cannot be left empty!')
            elif not re.match(r'^[a-zA-Z0-9]+$', data['password']):
                response.append('Password can only contain aplha numeric characters!')
            elif data['password'] != data['confirm_password']:
                response.append('Passwords entered do not match!')
            else:
                user.password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        elif data['type'] == 'description':
            if not data['description']:
                response.append('Description is empty!')
            else:
                user.desc = data['description']
        user.save()
        return response

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    level = models.IntegerField()
    objects = UsersManager()