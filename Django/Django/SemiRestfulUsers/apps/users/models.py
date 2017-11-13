# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Users first name cannot be blank"
        if len(postData['last_name']) <1:
            errors['last_name'] = "Users last name cannot be blank"
        if len(postData['email']) <1:
            errors['email'] = "Users email cannot be blank"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self): 
        return self.first_name + ' ' + self.last_name
