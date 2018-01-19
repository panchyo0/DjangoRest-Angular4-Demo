from rest_framework import serializers
from questionnaire.models import Questionnaire

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questionnaire
        fields=[
            'Id',
            'Create_at',
            'Name',
            'Age',
            'Address',
            'Email',
            'Phone_Number',
            'Do_you_like_open_source_software',
            'Python_level',
            'C_level',
            'Cpp_level',
            'Java_level',
            'JavaScript_level',
            'Which_computer_language_are_you_prefer',
        ]

class QuestionnaireCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questionnaire
        fields=[
            'Name',
            'Age',
            'Address',
            'Email',
            'Phone_Number',
            'Do_you_like_open_source_software',
            'Python_level',
            'C_level',
            'Cpp_level',
            'Java_level',
            'JavaScript_level',
            'Which_computer_language_are_you_prefer',
        ]
