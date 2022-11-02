from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rooms
from django.contrib.auth.models import User


import sys
print(sys.setrecursionlimit(1500))

@receiver(post_save, sender=Rooms)
def link_user(sender, instance, created, **kwargs):
    import inspect
    import requests
    import urllib.parse
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    
    try:
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(instance.address) +'?format=json'
        response = requests.get(url).json()
        lat=response[0]["lat"]
        lon=response[0]["lon"]
    except:
        lat=19.076
        lon=72.8777
    # print(response[0]["lat"])
    # print(response)
    if created:
        data=Rooms.objects.get(id=instance.id)
        data.owner=request.user

        data.lat=lat
        data.long=lon
        data.save()
    elif not created:
        data=Rooms.objects.filter(id=instance.id).update(owner=request.user,lat=lat,long=lon)
        # data.lat=lat
        # data.long=lon
        # data.save()

        

