# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
#Questionnaire models
class Questionnaire (models.Model):
    Id = models.AutoField(primary_key=True)
    Create_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    Name = models.CharField(max_length=5000)
    Age = models.CharField(max_length=5000)
    Address = models.CharField(max_length=5000)
    Email = models.CharField(max_length=5000)
    Phone_Number = models.CharField(max_length=5000)
    Do_you_like_open_source_software= models.CharField(max_length=5000)
    Python_level = models.CharField(max_length=5000)
    C_level = models.CharField(max_length=5000)
    Cpp_level = models.CharField(max_length=5000)
    Java_level = models.CharField(max_length=5000)
    JavaScript_level = models.CharField(max_length=5000)
    Which_computer_language_are_you_prefer = models.CharField(max_length=5000)
    class Meta():
    #setting questiong showing order according date
        ordering=["-Create_at"]

	def __str__(self):
		"""
        return poster name for each comment
		"""
		return self.Id
