from __future__ import unicode_literals
from django.db import models
import django.contrib.postgres
from django.contrib.postgres.fields import ArrayField,JSONField
import uuid
import datetime
from django.db import models
from django.contrib.auth.hashers import make_password


# class userDetails(models.Model):

# 	user_id = models.CharField(max_length=2000,null=True)
# 	broker = models.CharField(max_length=2000,null=True)
# 	email = models.EmailField(max_length=1000,blank=False,null=True)
# 	member_id = models.CharField(max_length=2000,null=True)
# 	user_name = models.CharField(max_length=2000,null=True)
# 	user_type = models.CharField(max_length=2000,null=True)
# 	exchange = JSONField(db_index=True,null=True)
# 	login_time = models.DateTimeField(blank=True,null=True)
# 	order_type = JSONField(db_index=True,null=True)
# 	product = JSONField(db_index=True,null=True)
# 	public_token = models.CharField(max_length=2000,null=True)
# 	password_reset = models.CharField(max_length=2000,null=True)


class bloctradeUser(models.Model):
	userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
	userName = models.CharField(max_length=2000,null=True)
	emailId = models.EmailField(max_length=2000,blank=False)
	password = models.CharField(max_length=2000,null=True)
	contactNumber = models.CharField(max_length=2000,null=True)
	role = models.CharField(max_length=2000,null=True)
	userStatus = models.CharField(max_length=2000,default='Active',null=True)

class userToken(models.Model):
	token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	userName = models.CharField(max_length=2000,null=True)
	date = models.DateField(default=django.utils.timezone.now, blank=True)


class conservative(models.Model):
	groupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	groupName = models.CharField(max_length=2000,null=True)
	groupDescription = models.TextField(null=True)
	groupType = models.CharField(max_length=2000,null=True)
	minimumAmount = models.BigIntegerField(null=True)
	indexValue = models.FloatField(null=True, blank=True, default=None)
	oneYearReturn = models.FloatField(null=True, blank=True, default=None)
	oneMonthReturn = models.FloatField(null=True, blank=True, default=None)
	stocks = ArrayField(models.CharField(max_length=1000), blank=True,null=True)

class moderate(models.Model):
	groupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	groupName = models.CharField(max_length=2000,null=True)
	groupDescription = models.TextField(null=True)
	groupType = models.CharField(max_length=2000,null=True)
	minimumAmount = models.BigIntegerField(null=True)
	indexValue = models.FloatField(null=True, blank=True, default=None)
	oneYearReturn = models.FloatField(null=True, blank=True, default=None)
	oneMonthReturn = models.FloatField(null=True, blank=True, default=None)
	stocks = ArrayField(models.CharField(max_length=1000), blank=True,null=True)
	
class aggressive(models.Model):
	groupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	groupName = models.CharField(max_length=2000,null=True)
	groupDescription = models.TextField(null=True)
	groupType = models.CharField(max_length=2000,null=True)
	minimumAmount = models.BigIntegerField(null=True)
	indexValue = models.FloatField(null=True, blank=True, default=None)
	oneYearReturn = models.FloatField(null=True, blank=True, default=None)
	oneMonthReturn = models.FloatField(null=True, blank=True, default=None)
	stocks = ArrayField(models.CharField(max_length=1000), blank=True,null=True)


class userGroup(models.Model):
	groupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	userId = models.UUIDField(null=True)
	groupName = models.CharField(max_length=2000,null=True)
	groupDescription = models.TextField(null=True)
	groupType = models.CharField(max_length=2000,null=True)
	minimumAmount = models.BigIntegerField(null=True)
	indexValue = models.FloatField(null=True, blank=True, default=None)
	oneYearReturn = models.FloatField(null=True, blank=True, default=None)
	oneMonthReturn = models.FloatField(null=True, blank=True, default=None)
	stocks = ArrayField(models.CharField(max_length=1000), blank=True,null=True)
	

class allShares(models.Model):

	stockId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	groupId = models.UUIDField(null=True)
	groupType = models.CharField(max_length=2000,null=True)
	stockName = models.CharField(max_length=2000,null=True)
	currentPrice = models.BigIntegerField(null=True)
	weightInPercentage = models.BigIntegerField(null=True)






