import imp
from attr import field

from django.contrib.auth.forms import UserCreationForm
from django import forms 

from django.contrib.auth.models import User
from .models import Foydalanuvchi


class CreateUserForm(UserCreationForm):
      class Meta:
          model = User
          fields = ['username','email','password1','password2'] 
          
          
          
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']         
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Foydalanuvchi
        fields = ['image']         

          