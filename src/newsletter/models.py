from django.contrib.auth.models import User
from django.db import models
from django import forms
from datetime import datetime

# Create your models here.
class signup(models.Model):
	email = models.EmailField(blank = False)
	full_name = models.CharField(max_length = 200,blank = True , null = True)
	time_stamp = models.DateTimeField(auto_now_add = True,auto_now = False)
	updated = models.DateTimeField(auto_now_add = False,auto_now = True)

	def __str__(self):
		return self.email

class sellerprofile(models.Model):	
    BATCH_CHOICES = (
        ('CSA', 'CSA'),
        ('CSB', 'CSB'),
        ('ECA', 'ECA'),
        ('ECB', 'ECB'),
        ('EEE', 'EEE'),
        ('BME', 'BME'),
    )
    PROJECT_TYPE = (
    	('MINI','MINIPROJECT'),
    	('MAIN','MAINPROJECT'),
    )
    seller = models.OneToOneField(User,on_delete=models.CASCADE,)
    project_title = models.CharField(max_length = 200,blank = True , null = True)
    batch = models.CharField(max_length = 200,choices = BATCH_CHOICES,blank = True , null = True)
    ptype = models.CharField(max_length = 200,choices = PROJECT_TYPE,blank = True , null = True)
    
    def __str__(self):
		return self.seller.username

class student_details(models.Model):
	name = models.CharField(max_length = 200)
	rollno = models.IntegerField()
	email = models.EmailField(blank = False)
	group = models.ForeignKey(sellerprofile,related_name = 'member')

class notifications(models.Model):
	idno = models.IntegerField(null = True)
	notification = models.CharField(max_length = 1000)
	category= models.CharField(max_length = 50,default='private')

class adminregister(models.Model):
    BATCH_CHOICES = (
        ('CSA', 'CSA'),
        ('CSB', 'CSB'),
        ('ECA', 'ECA'),
        ('ECB', 'ECB'),
        ('EEE', 'EEE'),
        ('BME', 'BME'),
    )
    PROJECT_TYPE = (
    	('MINI','MINIPROJECT'),
    	('MAIN','MAINPROJECT'),
    )
    faculty = models.OneToOneField(User)
    name = models.CharField(max_length = 200)
    Managing_class = models.CharField(max_length = 200,choices = BATCH_CHOICES,blank = True , null = True)
    project_type = models.CharField(max_length = 200,choices = PROJECT_TYPE,blank = True , null = True)

    def __str__(self):
		return self.faculty.username

class Document(models.Model):
    gpno = models.IntegerField(null = True)
    time_stamp = models.DateTimeField(auto_now_add = True,auto_now = False)
    doc_title = models.CharField(max_length = 200,)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    docdesc = models.CharField(max_length = 200)
