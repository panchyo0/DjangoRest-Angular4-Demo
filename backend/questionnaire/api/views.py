from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    )
from rest_framework.permissions import(
    IsAdminUser,
    AllowAny,
    )
from questionnaire.models import Questionnaire
from .serializers import (
    QuestionnaireSerializer,
    QuestionnaireCreateSerializer
    )

class QuestionnaireCreateAPIView(CreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class=QuestionnaireCreateSerializer
    permission_classes=[AllowAny]

class QuestionnaireListAPIView(ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class=QuestionnaireSerializer
    permission_classes=[AllowAny]

class QuestionnaireDetailAPIView(RetrieveAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class=QuestionnaireSerializer
    permission_classes=[IsAdminUser]
    lookup_field='Id'
