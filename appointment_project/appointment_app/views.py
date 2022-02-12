from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from appointment_app.models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer

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



from django.views.decorators.csrf import csrf_exempt



# @csrf_exempt
# def Student_2(request):
# 	if request.method=="POST":
# 		res 	= {}
# 		try:
# 			name 	= request.POST['name']
# 			city	= request.POST['city']
# 			marks 	= request.POST['marks']
# 			age 	= request.POST['age']
# 		except Exception as e:
# 			res['msg'] = f"Check the request {e}"
# 			return JsonResponse(res)

# 		# if len(name)<2 or len(city)<2:
# 		# 	print("Please fill the form correctly")
# 		# else:
# 		student_count = student.objects.filter(name=name).count()

# 		if student_count:
# 			res["msg"] = " student allreday there with the same name"
# 		else:
# 			Student_2 = student(name=name, city=city, marks=marks, age=age)
# 			Student_2.save()
# 			res['data'] = {"studen_name": Student_2.name, "student_age" : Student_2.age}

# 	return JsonResponse(res)



class Student_2(APIView):
	def post(self,request):
		res 	= {}
		try:
			name 	= request.data['name'] 
			city	= request.data['city']
			marks 	= request.data['marks']
			age 	= request.data['age']
		except Exception as e:
			res['msg'] = f"Check the request {e}"
			return Response(res)
		
		student_count = student.objects.filter(name=name).count()

		if student_count: # 0 -->False , 1,2,3... ---> True
			res["msg"] = "student allreday there with the same name"
		else:
			serializer 	= StudentSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				res['data'] = serializer.data
			else:
				res['msg']	= "Error in serializer is_valid"
		
		return Response(res)

		





# for fetch all the students using rest_framwork
class StudentList(APIView):
	def get(self, request):
		students = student.objects.all()  
		# queryset [<object 1>,<object 2>] also know as complesx data type to json --> serilization  
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)


# for fetch specific the students using rest_framwork
class StudentDetail(APIView):
	def get(self, request):
		pk 			= request.GET.get("pk")
		students	= student.objects.get(id=pk)
		serializer 	= StudentSerializer(students)
		return Response(serializer.data)



# for create new students using rest_framwork
class StudentCreate(APIView):
	def post(self, request):
		res = {}
		serializer 	= StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res['data'] = serializer.data
		else:
			res['msg']	= "Error in serializer is_valid"

		return Response(res)



		
# for update the student using rest_framwork
class StudentUpdate(APIView):
	def put(self, request):
		pk 			= request.data["id"]
		std			= student.objects.get(id=pk)
		serializer 	= StudentSerializer(instance = std, data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

# for delete the student using rest_framwork
class StudentDelete(APIView):
	def delete(self, request):
		pk 			= request.data["id"]
		std			= student.objects.get(id=pk)
		std.delete()
		return Response("ITEM DELETED SUCCESSFULLY")
		
