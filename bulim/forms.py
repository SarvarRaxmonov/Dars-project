import imp
from attr import field

from django.contrib.auth.forms import UserCreationForm
from django import forms 

from django.contrib.auth.models import User
from .models import Foydalanuvchi , IndexXat

class CreateUserForm(UserCreationForm):
      class Meta:
          model = User
          fields = ['username','email','password1','password2'] 
          
class IndexXatForm(forms.ModelForm):
      class Meta:
          model = IndexXat
          fields = ['ism','email','savol']
              

       
          
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']         
 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Foydalanuvchi
        fields = ['image']         

          