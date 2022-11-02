from rest_framework import serializers
from .models import *

class EmailSerializers(serializers.Serializer):
  email=serializers.EmailField()
  class Meta:
    fields=("email",)
    

class RoomSerializers(serializers.Serializer):
   class Meta:
      model=Rooms
      fields='__all__'