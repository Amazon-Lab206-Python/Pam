# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name must be at least 2 characters long")
        elif not str.isalpha(str(postData['first_name'])):
            errors.append("Please provide a valid first name")
        if len(postData['last_name']) < 2:
            errors.append("Last name must be at least 2 characters long")
        elif not str.isalpha(str(postData['last_name'])):
            errors.append("Please provide a valid last name")
        if len(postData['email']) < 1:
            errors.append("Users email cannot be blank")
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Please provide a valid email address")
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters in length")
        if len(postData['confirm_pass']) < 1:
            errors.append("Please confirm your password")
        elif postData['password'] != postData['confirm_pass']:
            errors.append("Passwords do not match")
        if len(errors) < 1:
            pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=pw_hash)
        return errors


    def validate_login(self, postData):
        errors = []
        if len(postData['email']) < 1:
            errors.append("Please provide your email address")
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Please provide a valid email address")
        if len(postData['password']) < 1:
            errors.append("Please provide your password")  
        if len(User.objects.filter(email=postData['email'])) == 0:
            errors.append("Unable to verify email/password combination. Please try again or register if you do not have an account")
        else:
            if not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()):
                errors.append("Unable to verify email/password combination. Please try again or register if you do not have an account")
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self): 
        return self.first_name +' '+ self.last_name