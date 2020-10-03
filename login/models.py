from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your models here.
class User_login(models.Model):
    user_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)




class blog_model(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    user = models.CharField(max_length=256)
    def __str__(self):
        return "test's Blog"

class comments(models.Model):
    user = models.CharField(max_length=256)
    content = models.TextField()
    blog = models.CharField(max_length=256)