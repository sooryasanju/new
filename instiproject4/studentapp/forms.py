from django.contrib.auth.forms import UserChangeForm
from adminapp.models import User
from django import forms

class EditProfileForm(forms.ModelForm):
    class Meta():
        model=User
        fields = ['user_name', 'user_address','user_mobile','user_email','user_username','user_password','image']
