from base.models import Question
from rest_framework import serializers

class QuesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
