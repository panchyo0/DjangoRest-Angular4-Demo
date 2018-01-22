from rest_framework import serializers
from questionnaire.models import Questionnaire
from questionnaire.models import Question

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=[
            'Question_1',
            'Question_2',
            'Question_3',
            'Question_4',
            'Question_5',
            'Question_6',
            'Question_7',
            'Question_8',
            'Question_9',
            'Question_10',
            'Question_11',
            'Question_12',
        ]

class QuestionnaireCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questionnaire
        fields=[
            'Answer_1',
            'Answer_2',
            'Answer_3',
            'Answer_4',
            'Answer_5',
            'Answer_6',
            'Answer_7',
            'Answer_8',
            'Answer_9',
            'Answer_10',
            'Answer_11',
            'Answer_12',
        ]
