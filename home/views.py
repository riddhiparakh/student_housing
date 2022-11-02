from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserform,Addproperty
from django.contrib.auth import login,authenticate, logout
from django.http import JsonResponse
from .models import *
from django.contrib import messages
from rest_framework import generics,status,viewsets,response
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from base64 import urlsafe_b64decode
from django.contrib.auth.decorators import login_required
from .filters import Roomfilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RoomSerializers
import simplejson as json

# Create your views here.
#no
#forgot password

def home(request):
  data=Rooms.objects.filter(duration='6 Months')
  room=Rooms.objects.all()
  room_filter=Roomfilter(request.GET,queryset=room)
  context={'filter':room_filter,'data':data}
  return render(request ,'index.html',context)

#login and signup(register) views
#sign up 
def register(request):
  form=CreateUserform()
  if request.method =='POST':
    form=CreateUserform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    
  context={'form':form}
  

  return render(request,'register.html',context)

#login
# def login_user(request):
  
  # if request.method=='POST':
  #   username=request.POST['username']
  #   password1=request.POST['password1']
   
  #   user=authenticate(request,username=username,password=password1)
  #   if user is not None:
  #     login(request,user)
  #     return redirect('home')
      
  #   else:
  #     return redirect('register')
      
  #   # if form.is_valid():
  #   #   form.save()
  # return render(request,'login.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)

            return redirect('house')

        else:
            return redirect("login")
    else:
        return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect('home')

@login_required(login_url='login')
def host(request):

  mydata=Rooms.objects.filter(owner=request.user)
  context={'data':mydata}
  return render(request ,'host.html',context) 




#room/hostels/pgs/property  view
def room_property(request):
  # get the properties of the current user
  # mydata=Rooms.objects.filter(request.user)
  mydata=Rooms.objects.all()
  context={'data':mydata}
  return render(request,'house.html',context)


# def api_room(request):
#   room_obj=Rooms.objects.all()
#   payload=[]
#   for room in room_obj:
#     result={}
  
#     result['bn']=room.building_name
#     result['add']=room.address
#     result['price']=room.price
#     result['preference']=room.preferences
#     result['room_image1']=room.room_image1
#     result['room_type']=room.room_type
#     result['capacity']=room.cap
#     result['food']=room.food
    
    
    
    
    
#     payload.append(result)
  
#   return JsonResponse(payload,safe=False,many=True)

#crud of rooms,hostel,property 
#create 
def AddProperty(request):
    form=Addproperty()
    
    if request.method == 'POST':
        # myData=Addproperty(request.POST)
        myData=Addproperty(request.POST, request.FILES)
        # print(myData)
        if myData.is_valid():
          myData.save()
          messages.success(request,'Property Added Successfully')
          return redirect('host')
        else:
          return redirect('home')
    context={"form":form}
    return render(request,'Addproperty.html',context)

#Read
def Propertydetail(request,room):
    # fetchdata=Rooms.objects.filter(building_name=room)#list
    fetchdata=Rooms.objects.get(building_name=room)
    latlon={
      "lat":fetchdata.lat,
      "lon":fetchdata.long,
    }
    print(latlon)
    latlonJSON=json.dumps(latlon)
    print(latlonJSON)
    context={"fetchdata":fetchdata, "data":latlonJSON}
    return render(request,'propertydetail.html',context)


#update 
def Propertyupdate(request,id):
    data=Rooms.objects.get(id=id)
    # updateform=Addproperty(request.POST or None,instance=data)
    updateform=Addproperty(request.POST or None, request.FILES or None, instance=data)
    if updateform.is_valid():
      updateform.save()
      messages.success(request,'Property Updated Successfully')
      return redirect('host')
    context={"form":updateform}
    return render(request,'Updateproperty.html',context)
    

    
#delete
def PropertyDelete(request,id):
    data=Rooms.objects.get(id=id)
    messages.warning(request,'Property Deleted Successfully')
    data.delete()
    return redirect('host')
  
  
def booknow(request):
  return render(request,'checkout.html')

def search(request):
  room=Rooms.objects.all()

  room_filter=Roomfilter(request.GET,queryset=room)
  rooms=room_filter.qs
  latlon=[]
  for i in rooms:
    coords=[]
    coords.append(i.lat)
    coords.append(i.long)
    coords.append(i.building_name)
    latlon.append(coords)
    

  latlonJSON=json.dumps(latlon)

  return render(request,'search.html', {"filter":room_filter, "data":latlonJSON})

 
 

@login_required(login_url='login')
def fav(request):
  return render(request,'fav.html')

def share(request):
  return render(request,'share.html')


@api_view(['GET','POST','PUT','PATCH'])
def getData(request):
  room=Rooms.objects.all()
  serializer=RoomSerializers(room,many=True)
  return Response(serializer.data) 


def setting(request):
  return render(request,'setting.html')