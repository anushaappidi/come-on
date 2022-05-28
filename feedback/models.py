from django.db import models
from django.contrib.auth.models import User
from django import forms
from user.models import Student

class Question(models.Model):
    Quality = models.CharField(max_length=30)
    def __str__(self):
        return self.Quality


class Feedback(models.Model):
    entry_by=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    answers = models.JSONField(null=True)
    def __str__(self):
        return self.entry_by.roll_no

       

   