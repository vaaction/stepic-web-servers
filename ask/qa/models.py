from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name='user_author')
    likes = models.ManyToManyField(User)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


class QuestionManager:
    def __init__(self):
        pass

    @staticmethod
    def new():
        return Question.objects.order_by(Question.added_at)[:10]

    @staticmethod
    def popular():
        return Question.objects.order_by(Question.rating)
