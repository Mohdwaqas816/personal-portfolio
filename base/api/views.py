from django.http import JsonResponse
from base.models import Question
from .serializers import QuesionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.api import serializers



@api_view(['GET'])
def votingData(request):
    questions = Question.objects.all()

    fullstack = Question.objects.filter(answer='fullstack').count()
    backend = Question.objects.filter(answer='backend').count()
    frontend = Question.objects.filter(answer='frontend').count()



    # serializer = QuesionSerializer(questions, many=True)


    return Response({'fullstack':fullstack, 'backend':backend, 'frontend':frontend})