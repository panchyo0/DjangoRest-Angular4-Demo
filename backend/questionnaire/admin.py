# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from .models import Questionnaire


# Register your models here.

class QuestionnaireAdmin(admin.ModelAdmin):
    """
    Set up question and answer in back end admin page
    """
    list_display=["Id","Create_at","Name","Age"]
    search_fields=["Create_at","Python_level"]
    list_filter=["Create_at"]

    class Meta:
        model=Questionnaire

admin.site.register(Questionnaire,QuestionnaireAdmin)
