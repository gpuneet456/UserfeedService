from django.http import response
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import UserFollow,Question,TopicFollow,QuestionTopic
from .serializers import QuestionSerializer
from .utils import dict_list_to_list_converter

# Create your views here.


@api_view()
@cache_page(60)
def get_userfeed(request,id):
    paginator = PageNumberPagination()
    paginator.page_size = 2
    followingIDQuerySet=UserFollow.objects.values('following_id').filter(follower_id=id)
    followingUsersQuesDictList=list(Question.objects.values('questionid').filter(userid_id__in=followingIDQuerySet).order_by('-timestamp'))
    followingUsersQuesList=dict_list_to_list_converter(followingUsersQuesDictList,'questionid')
    topicIDQuerySet=TopicFollow.objects.values('topic_id').filter(user_id=id)
    topicQuesQuerySet=QuestionTopic.objects.values('question_id').filter(topic_id__in=topicIDQuerySet)
    topicsQuesDictList=list(Question.objects.values('questionid').filter(questionid__in=topicQuesQuerySet).order_by('-timestamp'))
    topicsQuesList=dict_list_to_list_converter(topicsQuesDictList,'questionid')
    finalQuesIDList=followingUsersQuesList
    finalQuesIDList.extend(qid for qid in topicsQuesList if qid not in finalQuesIDList)
    finaQuesQuerySet=Question.objects.filter(questionid__in=finalQuesIDList)
    p=paginator.paginate_queryset(finaQuesQuerySet, request)
    serializer=QuestionSerializer(p,many=True)
    return paginator.get_paginated_response(serializer.data)