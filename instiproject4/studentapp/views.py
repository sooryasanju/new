from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import auth
from adminapp.models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr,Trainer,Feedback
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from studentapp.forms import EditProfileForm
from django.views import generic
from adminapp.models import Course
from Loginapp.forms import login_frm

# Create your views here.

class studentget_home(TemplateView):

    template_name = 'adminapp/studentbase.html'

class StudentFeedback(CreateView):
    model=Feedback

    fields=['user_username','batch_name','trainer_name','feedback_date','feedback_data']

    template_name = 'adminapp/studentfeedback.html'
    success_url=reverse_lazy('studentfeedback')



def view_profile(request):
    args={'user':request.session['user']}
    obj=User.objects.filter(user_username=args['user'])
    data={}
    data['object']=obj
    print(args)
    print("..................")
    return render(request,'adminapp/studentprofile.html',data)

class ProfileUpdate(UpdateView):
    model = User
    fields = ['user_name', 'user_address','user_mobile','user_email','user_username','user_password','image']
    template_name = 'adminapp/editprofile.html'
    success_url = reverse_lazy('stuprofile')

class StaffDetails(ListView):
    model = Trainer
    template_name = "adminapp/displaytrainer1.html"

def displaycomments(request):
    args = {'user': request.session['user']}
    print(args['user'])
    print("haiiiiiiiiiiiiidisplaycomments............")
    obj = User.objects.filter(user_username=args['user'])
    obj1 = Feedback.objects.filter(user_username=obj[0])
    print(obj1)
    data = {}
    data['object'] = obj1
    print(args)
    print("..................")
    return render(request, 'adminapp/displaycomment.html', data)

def studentlogout(request):
    del request.session['user']
    print("student logout sucessfully")
    #ob = login_frm()
    return render(request, 'adminapp/base.html')