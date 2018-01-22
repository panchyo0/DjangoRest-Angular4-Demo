# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
#question model
class Question(models.Model):
    """docstring for Question."""
    Question_Id = models.AutoField(primary_key=True)
    Question_Create_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    Question_1 = models.CharField(max_length=5000)
    Question_2 = models.CharField(max_length=5000)
    Question_3 = models.CharField(max_length=5000)
    Question_4 = models.CharField(max_length=5000)
    Question_5 = models.CharField(max_length=5000)
    Question_6= models.CharField(max_length=5000)
    Question_7 = models.CharField(max_length=5000)
    Question_8 = models.CharField(max_length=5000)
    Question_9 = models.CharField(max_length=5000)
    Question_10 = models.CharField(max_length=5000)
    Question_11 = models.CharField(max_length=5000)
    Question_12 = models.CharField(max_length=5000)
    class Meta():
    #setting questiong showing order according date
        ordering=["-Question_Create_at"]

	def __str__(self):
		"""
        return poster name for each comment
		"""
		return self.Question_Id


#Questionnaire models
class Questionnaire (models.Model):
    """docstring for Questionnaire's Answer."""
    Answer_Id = models.AutoField(primary_key=True)
    Answer_Create_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    Answer_1 = models.CharField(max_length=5000)
    Answer_2 = models.CharField(max_length=5000)
    Answer_3 = models.CharField(max_length=5000)
    Answer_4 = models.CharField(max_length=5000)
    Answer_5 = models.CharField(max_length=5000)
    Answer_6= models.CharField(max_length=5000)
    Answer_7 = models.CharField(max_length=5000)
    Answer_8 = models.CharField(max_length=5000)
    Answer_9 = models.CharField(max_length=5000)
    Answer_10 = models.CharField(max_length=5000)
    Answer_11 = models.CharField(max_length=5000)
    Answer_12 = models.CharField(max_length=5000)

    class Meta():
    #setting questiong showing order according date
        ordering=["-Answer_Create_at"]

	def __str__(self):
		"""
        return poster name for each comment
		"""
		return self.Answer_Id
