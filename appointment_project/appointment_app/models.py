from django.db import models
import datetime
# Create your models here.

class appointment(models.Model):
    title 			= models.CharField(max_length=255)
    date  			= models.DateField(("Date"), default=datetime.date.today)
    star_time 		= models.CharField(max_length=255)
    end_time 		= models.CharField(max_length=255)
    status 			= models.CharField(max_length=255)
    customer_name 	= models.CharField(max_length=255)
    agent_name 		= models.CharField(max_length=255)	


class school(models.Model):
    name           = models.CharField(max_length=255)
    address        = models.CharField(max_length=255)

class student(models.Model):
    name            = models.CharField(max_length=255)
    city            = models.CharField(max_length=255)
    age             = models.IntegerField()
    std             = models.CharField(max_length=255)
    marks           = models.FloatField(max_length=20)
    sch             = models.ForeignKey(school, on_delete=models.CASCADE)


# prpose of forign key
# 

    