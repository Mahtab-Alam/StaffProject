from django.db import models

# Create your models here.

class Staff(models.Model):
	fullname = models.CharField(max_length=100)
	email = models.EmailField()
	emp_code = models.CharField(max_length=12)
	company = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
