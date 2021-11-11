from django.db import models
from django.db.models.deletion import SET_DEFAULT

# Create your models here.
class User(models.Model):
    userid=models.CharField(max_length=36,editable=False,primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=12)

class Question(models.Model):
    questionid=models.CharField(max_length=36,editable=False,primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    text=models.CharField(max_length=300)
    upvotes=models.IntegerField()
    downvotes=models.IntegerField()
    timestamp=models.DateTimeField(auto_now=True)

class Topic(models.Model):
    topicid=models.CharField(max_length=36,editable=False,primary_key=True)
    name=models.CharField(max_length=30)   
    

class UserFollow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name="follower_set")
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name="following_set")

class QuestionTopic(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

class TopicFollow(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)