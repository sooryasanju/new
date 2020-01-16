from django.shortcuts import render
from .models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr
from django.views.generic import TemplateView, ListView
from django.views import generic
from adminapp.models import Course
# Create your views here.

class get_home(TemplateView):

    template_name = 'adminapp/base.html'


class get_about(TemplateView):

    template_name = 'adminapp/about-us.html'
class CourseList(ListView):
    model = Course
    template_name = 'adminapp/course.html'
class get_coursedetail(TemplateView):
    template_name = 'adminapp/course-details.html'
class get_contact(TemplateView):
    template_name = 'adminapp/contact.html'




