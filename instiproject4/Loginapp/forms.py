from django import forms

from adminapp.models import User


#class login_frm(forms.ModelForm):
    #class Meta():
        #model = User
        # exclude=[]
        # field = ()
        #field = ('user_name','user_password')
# ROLES= [
#      ('Student', 'Student'),
#      ('Trainer', 'Trainer'),
#      ('HR', 'HR'),
#      ]

class login_frm(forms.Form):
    # role = forms.ChoiceField(choices=ROLES,widget=forms.RadioSelect )
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
