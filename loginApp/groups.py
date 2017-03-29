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
from models import bloctradeUser,userToken
from models import conservative,moderate,aggressive,userGroup



class getConservativeGroup(APIView):

	#Fetching all goups

	def get(self, request,format=None):

		bloctradetoken = request.GET['bloctradetoken']

		try:

			userLoggedIn = userToken.objects.get(token__iexact=bloctradetoken)
			print "user is already loggedIn"
			
			try:

				allConservativeGroups = conservative.objects.all()

				result = []

				for group in allConservativeGroups:

					data = {}
					data['groupId'] = group.groupId
					data['groupName'] = group.groupName
					data['groupDescription'] = group.groupDescription
					data['indexValue'] = group.indexValue
					data['oneYearReturn'] = group.oneYearReturn
					data['minimumAmount'] = group.minimumAmount

					result.append(data)

				data = {'success':True,'msg':'Conservative groups fetched successfully',,'rows':result}
				return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type="application/json")

			except Exception,e:
				print str(e)
				data = {'success':False,'msg':'Error in fetching conservative groups'}
				return HttpResponse(json.dumps(data),content_type="application/json")

		except ObjectDoesNotExist:
			data ={'success':False,'msg':'Token does not exist please login'}
			return HttpResponse(json.dumps(data),content_type="application/json")



class getModerateGroup(APIView):

	#Fetching all the vendors selected for first Estimation

	def get(self, request,format=None):

		bloctradetoken = request.GET['bloctradetoken']

		try:

			userLoggedIn = userToken.objects.get(token__iexact=bloctradetoken)
			print "user is already loggedIn"
			
			try:

				allConservativeGroups = moderate.objects.all()

				result = []

				for group in allConservativeGroups:

					data = {}
					data['groupId'] = group.groupId
					data['groupName'] = group.groupName
					data['groupDescription'] = group.groupDescription
					data['indexValue'] = group.indexValue
					data['oneYearReturn'] = group.oneYearReturn
					data['minimumAmount'] = group.minimumAmount

					result.append(data)

				data = {'success':True,'msg':'Conservative groups fetched successfully','rows':result}
				return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type="application/json")

			except Exception,e:
				print str(e)
				data = {'success':False,'msg':'Error in fetching conservative groups'}
				return HttpResponse(json.dumps(data),content_type="application/json")

		except ObjectDoesNotExist:
			data ={'success':False,'msg':'Token does not exist please login'}
			return HttpResponse(json.dumps(data),content_type="application/json")


class getAggressiveGroup(APIView):

	#Fetching all the vendors selected for first Estimation

	def get(self, request,format=None):

		bloctradetoken = request.GET['bloctradetoken']

		try:

			userLoggedIn = userToken.objects.get(token__iexact=bloctradetoken)
			print "user is already loggedIn"
			
			try:

				allConservativeGroups = aggressive.objects.all()

				result = []

				for group in allConservativeGroups:

					data = {}
					data['groupId'] = group.groupId
					data['groupName'] = group.groupName
					data['groupDescription'] = group.groupDescription
					data['indexValue'] = group.indexValue
					data['oneYearReturn'] = group.oneYearReturn
					data['minimumAmount'] = group.minimumAmount

					result.append(data)

				data = {'success':True,'msg':'Conservative groups fetched successfully','rows':result}
				return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type="application/json")

			except Exception,e:
				print str(e)
				data = {'success':False,'msg':'Error in fetching conservative groups'}
				return HttpResponse(json.dumps(data),content_type="application/json")

		except ObjectDoesNotExist:
			data ={'success':False,'msg':'Token does not exist please login'}
			return HttpResponse(json.dumps(data),content_type="application/json")


class getUserGroup(APIView):

	#Fetching all the vendors selected for first Estimation

	def get(self, request,format=None):

		bloctradetoken = request.GET['bloctradetoken']

		try:

			userLoggedIn = userToken.objects.get(token__iexact=bloctradetoken)
			print "user is already loggedIn"
			
			try:

				allConservativeGroups = conservative.objects.all()

				result = []

				for group in allConservativeGroups:

					data = {}
					data['groupId'] = group.groupId
					data['groupName'] = group.groupName
					data['groupDescription'] = group.groupDescription
					data['indexValue'] = group.indexValue
					data['oneYearReturn'] = group.oneYearReturn
					data['minimumAmount'] = group.minimumAmount

					result.append(data)

				data = {'success':True,'msg':'Conservative groups fetched successfully','rows':result}
				return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type="application/json")

			except Exception,e:
				print str(e)
				data = {'success':False,'msg':'Error in fetching conservative groups'}
				return HttpResponse(json.dumps(data),content_type="application/json")

		except ObjectDoesNotExist:
			data ={'success':False,'msg':'Token does not exist please login'}
			return HttpResponse(json.dumps(data),content_type="application/json")									



