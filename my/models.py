from django.db import models

class userbio(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    

class userpost(models.Model):
    username=models.CharField(max_length=20)
    age=models.CharField(max_length=20,default=0)
