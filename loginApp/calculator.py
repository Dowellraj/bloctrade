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
# from models import userDetails
# from kiteconnect import KiteConnect
from django.core.serializers.json import DjangoJSONEncoder


class calculate(APIView):

	#Login
	def get(self, request,format=None):

		try:

	
			target = int(request.GET['target'])
			timeInYear = int(request.GET['timeInYear'])

			annualReturn = 0.11 # In percent
			monthlyReturn = 0.01 #In percent

			monthlyDeposit = target/(timeInYear*12*(1+0.01)**timeInYear)
			oneTimeDeposit = target/((1+0.11)**timeInYear)

			data = {'success':True,'msg':'calculated successfully','monthlyDeposit':monthlyDeposit,'oneTimeDeposit':oneTimeDeposit}
			return HttpResponse(json.dumps(data),content_type="application/json")

		except Exception,e:
			print str(e)
			data = {'success':False,'msg':'Erron in calculator'}
			return HttpResponse(json.dumps(data),content_type="application/json")


