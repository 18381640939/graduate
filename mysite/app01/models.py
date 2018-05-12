# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

class User(models.Model):
    username =  models.CharField(max_length=80)
    password = models.CharField(max_length=50)
    email = models.EmailField()
# Create your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')
admin.site.register(User,UserAdmin)