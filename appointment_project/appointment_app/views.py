from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from appointment_app.models import *
# Create your views here.


class Appointment(View):
	"""docstring for Appointment"""
	def get(self,request):
		# write code here
		return HttpResponse('lavish')

	def post(self,request):
		# data 	= json.loads(request.body.decode('utf-8'))
		# app_obj	= appointment(title=data['title'])					
		# app_obj.save()

		return HttpResponse('post method')



class Student(View):
	"""docstring for Appointment"""
	def get(self,request):

		return HttpResponse('lavish')


	def post(self,request):
		res = {
			"status" : False,
			"data"	 : None,
			"msg"	 : "Failed"
		}
		# here we will get the json data from post man as json string
		# u can not use directly json str over here
		# so we need to convert json str to dict using json.loads
		try:
			data 			= json.loads(request.body.decode('utf-8'))
			std_obj			= student()
			std_obj.name 	= data['name']
			std_obj.city 	= data['city']
			std_obj.age 	= data['age']
			std_obj.std 	= data['std']
			std_obj.marks 	= data['marks']
			std_obj.save()

			res['status'] 	= True
			res['data'] 	= data
			res['msg']		= "success"

		except Exception as e:
			res['msg']		= e

		return HttpResponse(str(res))



class StudentGreaterThan(View):
	"""docstring for Appointment"""
	def get(self,request):
		res = {
			"status" : False,
			"data"	 : [],
			"msg"	 : "Failed"
		}

		try:
			data = json.loads(request.body.decode('utf-8'))

			if "product_name" in data:
				students 		= 	list(student.objects.filter(city=data['product_name']).values_list('name', flat=True))
				
				res['data'] 	=   students
				res['status'] 	= 	True
				res['msg']		= 	"success"
			else:
				res['msg'] = "Invalid Request"

		except Exception as e:
			res['msg']	= e

		return HttpResponse(str(res))


class GetSchoolDetails(View):
	"""docstring for Appointment"""
	def get(self,request):
		res = {
			"status" : False,
			"data"	 : {},
			"msg"	 : "Failed"
		}

		try:
			data = json.loads(request.body.decode('utf-8'))

			if "std_name" in data:
				Student = student.objects.get(name=data['std_name'])

				res['data']['std_name'] 	=   Student.name
				res['data']['age'] 			=   Student.age

				res['data']['sch_name'] 	=   Student.sch.name
				res['data']['sch_adress'] 	=   Student.sch.address

				res['status'] 	= 	True
				res['msg']		= 	"success"
			else:
				res['msg'] = "Invalid Request"

		except Exception as e:
			res['msg']	= e

		return HttpResponse(str(res))