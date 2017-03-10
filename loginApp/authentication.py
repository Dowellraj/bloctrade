#Auther --> Piyush S. Wanare
#Designation --> Freelance Developer

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
import uuid
import django.utils.timezone
import datetime
from models import userDetails
from kiteconnect import KiteConnect
from django.core.serializers.json import DjangoJSONEncoder

class loginurl(APIView):

	def get(self, request,format=None):

		api_key = 'nn71s9xaq8cbh5yi'

		try:
			kite = KiteConnect(api_key=api_key)
			url = kite.login_url()

			data = {'success':True,'msg':'Login url fetched successfully','url':url}
			return HttpResponse(json.dumps(data),content_type="application/json")

		except Exception,e:
			print str(e)
			data = {'success':False,'msg':str(e)}
			return HttpResponse(json.dumps(data),content_type="application/json")


class authentication(APIView):

	def get(self, request,format=None):

		api_secret = 'yz4lae5oyv4sa4w324rxgfjumo5ajsbg'
		requestToken = request.GET['requestToken']

		try:
			data = kite.request_access_token(requestToken,api_secret)

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

			updateUserMyDatabase = userDetails.object.update_or_create(user_id=data['user_id'],defaults={'email':data['email'],
				'broker':data['broker'],'member_id':data['member_id'],'user_name':data['user_name'],
				'user_type':data['user_type'],'exchange':data['exchange'],'login_time':data['login_time'],
				'order_type':data['order_type'],'order_type':data['order_type'],'product':data['product'],
				'public_token':data['public_token'],'password_reset':data['password_reset']})


			data = {'success':True,'msg':'access token fetched successfully','data':data}
			return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type="application/json")

		except Exception,e:
			print str(e)
			data = {'success':False,'msg':str(e)}
			return HttpResponse(json.dumps(data),content_type="application/json")

