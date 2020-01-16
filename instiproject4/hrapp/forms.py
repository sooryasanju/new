from django import forms
from adminapp.models import User,Trainer
from adminapp.models import TimeTable

class Student_form(forms.ModelForm):
    class Meta():
        model = User
        fields ='__all__'

class Trainer_form(forms.ModelForm):
    class Meta():
        model = Trainer
        fields ='__all__'
class displaystudent_form(forms.ModelForm):
    class Meta():
        model = User
        fields =['course_name','batch_name']
class displaytrainer_form(forms.ModelForm):
    class Meta():
        model = Trainer
        fields ='__all__'


class time_frm(forms.ModelForm):
    class Meta():
        model = TimeTable
        # exclude=[]
        # field = ()
        fields=['batch_name','class_name','start_time','end_time']



