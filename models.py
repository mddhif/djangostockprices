from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.conf import settings
from datetime import date




class Prices(models.Model):
	symbol = models.CharField(db_column='Symbol', max_length=6)  # Field name made lowercase.
	datex = models.DateTimeField(db_column='Date', default=date.today)  # Field name made lowercase.
	open = models.FloatField(db_column='Open')  # Field name made lowercase.
	high = models.FloatField(db_column='High')  # Field name made lowercase.
	low = models.FloatField(db_column='Low')  # Field name made lowercase.
	close = models.FloatField(db_column='Close')  # Field name made lowercase.
	volume = models.IntegerField(db_column='Volume')  # Field name made lowercase.
	adjclose = models.FloatField(db_column='Adjclose')  # Field name made lowercase.

	
	
	
	
	def __str__(self):
		return self.symbol

	class Meta:
		managed = False
		db_table = 'Prices'



class User(models.Model):
	username = models.CharField(db_column='Username', max_length=15)
	email = models.EmailField(db_column='Email')
	password = models.CharField(db_column='Password', max_length=15)

	class Meta:
		managed = False
		db_table = 'User'