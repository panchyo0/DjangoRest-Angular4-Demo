# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from .models import Questionnaire
from .models import Question



# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    """docstring for QuestionAdmin."""
    list_display=["Question_Id","Question_Create_at"]
    search_fields=["Question_Create_at"]
    list_filter=["Question_Create_at"]

    class Meta:
        model=Question
admin.site.register(Question,QuestionAdmin)


class QuestionnaireAdmin(admin.ModelAdmin):
    """
    Set up question and answer in back end admin page
    """
    list_display=["Answer_Id","Answer_Create_at"]
    search_fields=["Answer_Create_at"]
    list_filter=["Answer_Create_at"]

    class Meta:
        model=Questionnaire
    def has_add_permission(self, request):
        return False
admin.site.register(Questionnaire,QuestionnaireAdmin)
