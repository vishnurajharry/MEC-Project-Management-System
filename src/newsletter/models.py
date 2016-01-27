from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
class signup(models.Model):
	email = models.EmailField(blank = False)
	full_name = models.CharField(max_length = 200,blank = True , null = True)
	time_stamp = models.DateTimeField(auto_now_add = True,auto_now = False)
	updated = models.DateTimeField(auto_now_add = False,auto_now = True)

	def __str__(self):
		return self.email

class sellerprofile(models.Model):	
    # year = models.IntegerField()
    seller = models.OneToOneField(User,on_delete=models.CASCADE,)
    company = models.CharField(max_length = 200,blank = True , null = True)
    addressline1 = models.CharField(max_length = 200,blank = True , null = True)
    addressline2 = models.CharField(max_length = 200,blank = True , null = True)
	
    def __str__(self):
		return self.seller.username

class notifications(models.Model):
	idno = models.IntegerField()
	notification = models.CharField(max_length = 1000)