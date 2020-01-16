from django.shortcuts import render
from django.shortcuts import render
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from Loginapp.forms import login_frm
from adminapp.models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr,Trainer
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from hrapp.forms import Student_form,Trainer_form,displaystudent_form,displaytrainer_form
from django.contrib import auth
# Create your views here.


class hrget_home(TemplateView):

    template_name = 'adminapp/hrbase.html'



def get_register(request):
    if request.method=='GET':
        obj=Student_form()
        return render(request, 'adminapp/studentregister.html', {'form':obj})
    if request.method=='POST':
        form=Student_form(request.POST,request.FILES)

        if form.is_valid():
            name = form.cleaned_data['user_name']
            address=form.cleaned_data['user_address']
            mobile=form.cleaned_data['user_mobile']
            doj=form.cleaned_data['user_doj']
            email=form.cleaned_data['user_email']
            username=form.cleaned_data['user_username']
            user_password=form.cleaned_data['user_password']
            confirmpassword=form.cleaned_data['confirm_password']
            coursename=form.cleaned_data['course_name']
            batchname=form.cleaned_data['batch_name']
            userpayment=form.cleaned_data['user_payment']
            rolename=form.cleaned_data['role_name']
            img=form.cleaned_data['image']
            print(img)

        try:
            # obj = User(username=name,email=email1, address=address1, password=passw1,coursename=course1,batch=batch1)
            form.save()
        except Exception as e:
            print(e.args)
        obj = Student_form()
        return render(request,  'adminapp/studentregister.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"


def get_trainer(request):
    if request.method == 'GET':
        obj = Trainer_form()
        return render(request, 'adminapp/trainerregister.html', {'form': obj})
    if request.method == 'POST':
        form = Trainer_form(request.POST)

        if form.is_valid():
            coursename = form.cleaned_data['course_name']
            trainername=form.cleaned_data['trainer_name']
            trainermobile = form.cleaned_data['trainer_mobile']
            trainerdoj = form.cleaned_data['trainer_doj']
            traineremail = form.cleaned_data['trainer_email']
            trainerusername = form.cleaned_data['trainer_username']
            trainerpassword = form.cleaned_data['trainer_password']
            rolename = form.cleaned_data['role_name']

        try:
            # obj = User(username=name,email=email1, address=address1, password=passw1,coursename=course1,batch=batch1)
            form.save()
        except Exception as e:
            print(e.args)
        obj = Trainer_form()
        return render(request, 'adminapp/trainerregister.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"




def display_student(request):
    if request.method=='GET':
        obj=displaystudent_form()
        return render(request, 'adminapp/displaystudent1.html', {'form':obj})
    if request.method=='POST':
        form=displaystudent_form(request.POST)

        if form.is_valid():
            course1 =form.cleaned_data['course_name']
            batch1=form.cleaned_data['batch_name']
            print(course1)
            print(batch1)
            type(course1)
            type(batch1)


        try:
            obj=User.objects.filter(course_name=course1)
            print("''''''''''''''''")
            obj1=obj.filter(batch_name=batch1)
            print("----------------------------")
            data = {}
            print(obj1)
            data['object'] = obj1


            return render(request, 'adminapp/displaystudent.html',data)
        except Exception as e:
            print(e.args)
        obj = displaystudent_form()
        return render(request,  'adminapp/displaystudent1.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"

# class StudentList(ListView):
#     model = User
#     template_name = 'adminapp/displaystudent.html'


class StudentUpdate(UpdateView):
    model = User
    fields=['user_name','user_address','course_name','batch_name','user_payment']
    template_name = 'adminapp/studentedit.html'
    success_url = reverse_lazy('displaystudent')
class StudentDelete(DeleteView):
    model = User
    fields='__all__'
    template_name = 'adminapp/studentdelete.html'
    success_url = reverse_lazy('displaystudent')


class TrainerList(ListView):
    model = Trainer
    template_name = 'adminapp/displaytrainer.html'


class TrainerUpdate(UpdateView):
    model = Trainer
    fields=['course_name','trainer_name','trainer_mobile','trainer_email']
    template_name = 'adminapp/traineredit.html'
    success_url = reverse_lazy('displaytrainer')
class TrainerDelete(DeleteView):
    model = Trainer
    fields='__all__'
    template_name = 'adminapp/trainerdelete.html'
    success_url = reverse_lazy('displaytrainer')

def hrlogout(request):

    del request.session['user']
    print("hr logout sucessfully")
    #ob =login_frm()
    return render(request, 'adminapp/base.html')
    #return redirect('home')

from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import time
from adminapp.models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr,Trainer
from django.views.generic import TemplateView, ListView, CreateView
from django.views import generic
from adminapp.models import Course
# Create your views here.
from hrapp.forms import time_frm
from django.db.models import Q

class hrget_home(TemplateView):

    template_name = 'adminapp/hrbase.html'

class UserCreate(CreateView):
    model=User
    fields='__all__'
    template_name = 'adminapp/studentregister.html'
    success_url=reverse_lazy('studentregister')

# class studentList(ListView):
#     model = User
 #template_name = 'adminapp/studentregister.html'

class TrainerCreate(CreateView):
    model=Trainer
    fields='__all__'
    template_name = 'adminapp/trainerregister.html'
    success_url=reverse_lazy('trainerregister')



def timetable(request):
    if request.method =='GET':
        form = time_frm()


    if request.method == 'POST':
        form = time_frm(request.POST)
        if form.is_valid():
                print("form is valid")
                classname = form.cleaned_data['class_name']
                st = form.cleaned_data['start_time']
                et = form.cleaned_data['end_time']
                # print(classname)
                # print(st)
                # print(et)
                # print(TimeTable.objects.filter(class_name=classname))
                # if TimeTable.objects.filter(class_name=classname).filter(Q(start_time__range=(st,et)) | Q(end_time__range=(st,et))):
                #     print("class not available")


                if TimeTable.objects.filter(class_name=classname).filter(start_time__lt=st).filter(end_time__gt=st):
                         print("class not available for this time slot")
                elif TimeTable.objects.filter(class_name=classname).filter(start_time__lt=et).filter(end_time__gt=et):
                         print("class not available for this time slot")
                elif TimeTable.objects.filter(class_name=classname).filter(start_time__gt=st).filter(start_time__lt=et):
                         print("class not available for this time slot")
                elif TimeTable.objects.filter(class_name=classname).filter(end_time__gt=st).filter(end_time__lt=et):
                         print("class not available for this time slot")
                else:
                        form.save(commit=True)
                        print("saved")
                        # p = TimeTable.objects.all()
                        # print(p)

        else:
                print("ERROR")

    return render(request, 'adminapp/timetable.html', {'form': form})

class Job_form(ModelForm):
    class Meta():
        model=Placement
        fields='__all__'
def add_jobs(request):
    if request.method=='GET':
        form=Job_form()
        return render(request, 'hrapp/placement.html', {'form': form})
    if request.method=='POST':
        form=Job_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
    form = Job_form()
    return render(request, 'hrapp/placement.html', {'form': form})

class List_jobs(ListView):
    model = Placement
    template_name = 'hrapp/joblist.html'

