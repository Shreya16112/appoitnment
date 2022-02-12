"""appointment_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views


urlpatterns = [
    path('create_slot/', csrf_exempt(views.Appointment.as_view())),
    path('create_std/', csrf_exempt(views.Student.as_view())),
    path('greater_than_number/', views.StudentGreaterThan.as_view()),
    path('get_school_details/', views.GetSchoolDetails.as_view()),
    path('student/', views.Student_2.as_view()),

    path('student_list/', views.StudentList.as_view()),
    path('student_detail/', views.StudentDetail.as_view()),
    path('student_create/', csrf_exempt(views.StudentCreate.as_view())),
    path('student_update/', csrf_exempt(views.StudentUpdate.as_view())),
    path('student_delete/', csrf_exempt(views.StudentDelete.as_view())),

]
