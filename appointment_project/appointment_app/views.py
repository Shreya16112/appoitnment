from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.


class Appointment(View):
	"""docstring for Appointment"""
	def get(self,request):
		return HttpResponse('get')

	def post(self,request):
		return HttpResponse('post')
