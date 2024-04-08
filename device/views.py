from django.shortcuts import render, HttpResponse, redirect
from .mongodb import MongoDBProcessor
from .mysql import MysqlProcessor

def addDevice(request):
    request_index = "1"
    # add device info
    mongodb = MongoDBProcessor()
    mysql = MysqlProcessor()
    deviceInfo = mongodb.get_camera_info(request_index)
    if mysql.add_device(deviceInfo):
        return HttpResponse('Device added')
    else:
        return HttpResponse('Device already exists')

def UpdateDeviceInfo(request):
    request_index = "1"
    # update device info
    mongodb = MongoDBProcessor()
    mysql = MysqlProcessor()
    deviceInfo = mongodb.get_camera_info(request_index)
    mysql.update_device_info(deviceInfo)
    
    return HttpResponse('Device info updated')

def getDeviceInfo(request):
    request_index = "1"
    # get device info
    db = MysqlProcessor()
    device_info = db.get_device_info(request_index)
    if device_info:
        return HttpResponse(device_info)
    else:
        return HttpResponse('Device not found')

def deleteDevice(request):
    request_index = "1"
    # delete device info
    db = MysqlProcessor()
    if db.delete_device(request_index):
        return HttpResponse('Device deleted')
    else:
        return HttpResponse('Device not found')

def updateImage(request):
    request_index = "1"
    # update image url
    mongodb = MongoDBProcessor()
    image_url = mongodb.get_image_url(request_index)
    db = MysqlProcessor()
    if db.updateImage(request_index, image_url):
        return HttpResponse('Image updated')
    else:
        return HttpResponse('Device not found')

def disableDevice(request):
    request_index = "1"
    # disable device
    db = MysqlProcessor()
    if db.disable_device(request_index):
        return HttpResponse('Device disabled')
    else:
        return HttpResponse('Device not found')

def get_device_of_district(request):
    district = "1"
    # get device info of district
    db = MysqlProcessor()
    devices = db.get_all_devices_of_district(district)
    print(devices)
    return HttpResponse(devices)