from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new():
        return Question.objects.order_by(Question.added_at)[:10]

    def popular():
        return Question.objects.order_by(Question.rating)


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='user_author')
    likes = models.ManyToManyField(User)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)