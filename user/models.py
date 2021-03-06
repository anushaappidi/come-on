from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    roll_no= models.CharField(max_length=100)
    student_name= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.student_name.username


class Teacher(models.Model):
    roll_no= models.CharField(max_length=100)
    teacher_name= models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    def __str__(self):
        return self.roll_no
        