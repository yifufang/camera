from django.shortcuts import render, HttpResponse, redirect
from .models import Device
from .mongodb import DBProcessor

# get device info
def UpdateDeviceInfo(request):
    request_index = "1"
    db = DBProcessor()
    device_info = db.get_camera_info(request_index)
    
    if device_info:
        if Device.objects.filter(index=device_info['index']).exists():
            device_mysql = Device.objects.get(index=device_info['index'])
            device_mysql.latitude = device_info['latitude']
            device_mysql.longitude = device_info['longitude']
            device_mysql.image_url = device_info['image_url']
            device_mysql.address = device_info['address']
            device_mysql.district = device_info['district']
            device_mysql.time = device_info['time']
            device_mysql.save()
        else:
            device_mysql = Device(index=device_info['index'], latitude=device_info['latitude'], longitude=device_info['longitude'], image_url=device_info['image_url'], address=device_info['address'], time=device_info['time'] ,district=device_info['district'])
            device_mysql.save()
        return HttpResponse('Device info updated')
        
    else:
        return HttpResponse('Device disabled')