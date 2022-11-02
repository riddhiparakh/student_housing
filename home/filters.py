import django_filters
from django_filters import CharFilter,ChoiceFilter
from .models import *

class Roomfilter(django_filters.FilterSet):
  # location=CharFilter(field_name="address",lookup_expr="icontains")
  type=(
     ('1','Shared room'),
    ('2','Private room')
    
  )
  room_type=ChoiceFilter(choices=type)
  class Meta:
    model=Rooms
    # fields="__all__"
    fields={
      'room_type':['exact'],
      'address':['icontains'],
      'duration':['exact'],
      'price':['lt']
    }
    # exclude=['building_name','cap','room_image','']
   