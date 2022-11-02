from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Rooms

class CreateUserform(UserCreationForm):
  # email=forms.CharField(max_length=50)
  class Meta:
    model=User
    fields=['username', 'email', 'password1', 'password2']
    # fields="__all__"

class Addproperty(forms.ModelForm):
  class Meta:
    model=Rooms
    fields=['building_name','address','price','room_image1','room_image2','room_image3','preferences','room_type','cap','food','duration']
    # fields="__all__"

# class roomfilter(forms.)
# class Updateproperty(forms.ModelForm):
#   class Meta:
#     model=Rooms
#     fields="__all__"
# class LoginUser(UserCreationForm):
#   class Meta:
#     model=User
#     fields=['username','password1']
  