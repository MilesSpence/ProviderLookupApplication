import datetime
from django.db import models
from django.utils import timezone
from postgres_copy import CopyManager

class ProviderFull(models.Model):
	npi = models.CharField(max_length=15, db_index=True)
	firstname = models.CharField(max_length=40, db_index=True)
	lastname = models.CharField(max_length=40, db_index=True)
	classification = models.CharField(max_length=100, db_index=True)
	mailingAddress = models.CharField(max_length=50, blank=True)
	mailingCityState = models.CharField(max_length=35, blank=True)
	mailingZipcode = models.CharField(max_length=25, blank=True, null=True)
	phone = models.CharField(max_length=25, blank=True, null=True)
	gender = models.CharField(max_length=10, blank=True, null=True)
	businessAddress = models.CharField(max_length=35, blank=True)
	businessCity = models.CharField(max_length=25, db_index=True)
	businessZipcode = models.CharField(max_length=15, db_index=True)
	businessCountry = models.CharField(max_length=25, blank=True, null=True)
	grouping = models.CharField(max_length=200, blank=True)
	definition = models.CharField(max_length=2400, blank=True)
	businessName = models.CharField(max_length=50, blank=True, null=True)
	fax = models.CharField(max_length=25, blank=True, null=True)
	businessState = models.CharField(max_length=16, db_index=True)
	# This is used for saving data to the Django ORM in views.py #
	objects = CopyManager()