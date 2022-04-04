import email
from statistics import mode
from turtle import Turtle
from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(
        max_length=30,blank=False,null=False)
    email = models.EmailField(
        max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(
        max_length=15,blank=False,null=False
    )
    confirm_password = models.CharField(
        max_length=15,null=False,blank=False
    )
    hint_question_options = [
        ('first school name','First School Name'),
        ('pet name','Pet Name'),
        ('teacher name','Teacher Name'),
        ('favorate food','Favorate Food'),
        ('collage name','Collage Name')
    ]

    hint_question = models.CharField(
        max_length=30, blank=False, null=False,
        choices=hint_question_options,
    )

    hint_answer = models.CharField(
        max_length=30,blank=True,null=True
    )