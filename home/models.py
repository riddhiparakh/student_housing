from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class User(models.Model):
#   name=models.CharField(max_length=100)
#   phone=models.IntegerField()
#   email=models.CharField(max_length=100,null=True,blank=True)
#   address=models.CharField(max_length=200)
#   created_at=models.DateTimeField(auto_now=True)
#   updated_at=models.DateTimeField(auto_now_add=True)

  # def __str__(self):
  #   return self.name
  # class Meta:
  #   verbose_name_plural="User"

# class Host(models.Model):
#   name=models.CharField(max_length=100)
#   phone=models.IntegerField()
#   email=models.CharField(max_length=100,null=True,blank=True)
#   address=models.CharField(max_length=200)
  
#   created_at=models.DateTimeField(auto_now=True)
#   updated_at=models.DateTimeField(auto_now_add=True)
   
class Room_Type(models.Model):
  type=[
    ('Shared room','Shared room'),
    ('pvt room','Private room')]
  name=models.CharField(max_length=100,choices=type, null=True)
  
  def __str__(self):
    return self.name
  
class Capacity(models.Model):
  cap=models.IntegerField()
  
  def __str__(self):
      return str(self.cap)
    
class Food(models.Model):
  food=models.CharField(max_length=50, null=True)
  
  def __str__(self):
    return self.food
  
class Preferences(models.Model):
  name=models.CharField(max_length=100, null=True)
  
  def __str__(self):
    return self.name
  
  # room_type=[
  #   ('Shared room','Shared room'),
  #   ('pvt room','Private room')]
  
  # no_roommate=[
  #   (1,1),
  #   (2,2),
  #   (3,3),
  #   (4,4),
  #   (5,5)]
  
  # food=[
  #   ('veg','Vegetarian'),
  #   ('non-veg','Non-vegetarian'),
  #   ('none','none')
  # ]
  
  # emenities=[
  #   ('Common TV room','Common TV room'),
  #   ('common reading room','Common reading room'),
  #   ('Dining Facilities','Dining Facilities'),
  #   ('Free wifi','Free Wifi'),
  #   ('gym','Gym'),
  #   ('house help','House help'),
  #   ('washing machine','Washing Machine'),
  #   ('electricity','Electricity'),
  #   ('gas','Gas'),
  #   ('24-hour running water','24-hour running water'),
  #   ('only few hours runnimg water','Only few hours running water'),
  #   ]
  
  # room=models.CharField(max_length=50,choices=room_type,default='shared room')
  # roommate_no=models.IntegerField(choices=no_roommate,default=1)
  # preferred_cusine=models.CharField(max_length=50,choices=food,null=True,blank=True)
  # eminity1=models.CharField(max_length=100,choices=emenities)
  # eminity2=models.CharField(max_length=100,choices=emenities)
  # eminity3=models.CharField(max_length=100,choices=emenities)
  # eminity4=models.CharField(max_length=100,choices=emenities,null=True,blank=True)
  # eminity5=models.CharField(max_length=100,choices=emenities,null=True,blank=True)
  # eminity6=models.CharField(max_length=100,choices=emenities,null=True,blank=True)
  # eminity7=models.CharField(max_length=100,choices=emenities,null=True,blank=True)
  # created_at=models.DateTimeField(auto_now=True)
  # updated_at=models.DateTimeField(auto_now_add=True)

    

  
  
  def __str__(self):
      return str(self.name)
  class Meta:
    verbose_name_plural="Preference"
 
 
class Rooms(models.Model):

  
  
  building_name=models.CharField(max_length=100)
  address=models.CharField(max_length=500)
  # city=models.CharField(max_length=500)
 
  # preference_id=models.ForeignKey(Preferences, on_delete=models.CASCADE)
  price=models.IntegerField(null=True)

  room_image1=models.ImageField(upload_to='img/', null=True)
  room_image2=models.ImageField(upload_to='img/', null=True)
  room_image3=models.ImageField(upload_to='img/', null=True)
  
  
  preferences=models.ManyToManyField(Preferences)
  room_type=models.ManyToManyField(Room_Type)
  cap=models.ManyToManyField(Capacity)
  food=models.ManyToManyField(Food)
  type=[
    ('6 Months','6 Months'),
    ('1 Year','1 Year'),
    ('2 Years','2 Years'),
  ]
  duration=models.CharField(choices=type, default='6 Months', max_length=30)
  owner=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  
  lat=models.DecimalField(max_digits=11, decimal_places=7, null=True)
  long=models.DecimalField(max_digits=11, decimal_places=7, null=True)
  
  
  def __str__(self):
      return self.building_name
  class Meta:
    verbose_name_plural="Rooms"
    

