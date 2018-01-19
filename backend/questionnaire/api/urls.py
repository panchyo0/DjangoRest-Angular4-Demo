from django.conf.urls import url
from django.contrib import admin

from .views import(
    QuestionnaireListAPIView,
    QuestionnaireDetailAPIView,
    QuestionnaireCreateAPIView,
    )

urlpatterns = [
    url(r'^$',QuestionnaireListAPIView.as_view(), name='list'),
    url(r'^create/$',QuestionnaireCreateAPIView.as_view(), name='create'),
    url(r'^(?P<Id>\d+)/$',QuestionnaireDetailAPIView.as_view(), name='detail'),
]
