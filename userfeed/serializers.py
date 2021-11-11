from rest_framework import serializers
from .models import User

class QuestionSerializer(serializers.Serializer):
    questionid=serializers.CharField(max_length=36)
    title=serializers.CharField(max_length=150)
    text=serializers.CharField(max_length=300)
    upvotes=serializers.IntegerField()
    downvotes=serializers.IntegerField()
    timestamp=serializers.DateTimeField()
    userid=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )