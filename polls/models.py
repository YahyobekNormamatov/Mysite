from django.db import models
import datetime

# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(datetime.datetime.now)

    def __str__(self):
        return
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
