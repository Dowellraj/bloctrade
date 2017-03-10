from __future__ import unicode_literals
from django.db import models
import django.contrib.postgres
from django.contrib.postgres.fields import ArrayField,JSONField
import uuid
import datetime
from django.db import models
from django.contrib.auth.hashers import make_password


class userDetails(models.Model):

	user_id = models.CharField(max_length=2000,null=True)
	broker = models.CharField(max_length=2000,null=True)
	email = models.EmailField(max_length=1000,blank=False,null=True)
	member_id = models.CharField(max_length=2000,null=True)
	user_name = models.CharField(max_length=2000,null=True)
	user_type = models.CharField(max_length=2000,null=True)
	exchange = JSONField(db_index=True,null=True)
	login_time = models.DateTimeField(blank=True,null=True)
	order_type = JSONField(db_index=True,null=True)
	product = JSONField(db_index=True,null=True)
	public_token = models.CharField(max_length=2000,null=True)
	password_reset = models.CharField(max_length=2000,null=True)
