from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from hrapp.forms import displaystudent_form
from adminapp.models import User, Trainer, Feedback
from django.urls import reverse_lazy
from Loginapp.forms import login_frm
from django.contrib import auth
# Create your views here.
class trainerget_home(TemplateView):

    template_name = 'adminapp/trainerbase.html'

def student_display(request):
    if request.method=='GET':
        obj=displaystudent_form()
        return render(request, 'adminapp/trainerdisplaystudent1.html', {'form':obj})
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


            return render(request, 'adminapp/trainerdisplaystudent.html',data)
        except Exception as e:
            print(e.args)
        obj = displaystudent_form()
        return render(request,  'adminapp/trainerdisplaystudent1.html', {'form': obj})
        msg = "Data Inserted Sucessfully!!!!!!!!1"

def viewstudentfeedback(request):
    args = {'user': request.session['user']}
    obj = Trainer.objects.filter(trainer_username=args['user'])
    print(obj[0])
    obj1=Feedback.objects.filter(trainer_name=obj[0])
    print("................")
    data1={}
    data1['object']=obj1

    return render(request, 'adminapp/trainerviewfeedback.html', data1)


class AddComment(UpdateView):
    model = Feedback
    fields = ['feedback_comment']
    template_name = 'adminapp/addcomment.html'
    success_url = reverse_lazy('viewfeedback')


def trainerlogout(request):
    del request.session['user']
    print("trainer logout sucessfully")

    return render(request, 'adminapp/base.html')