from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .mongodb import MongoDBProcessor
from .mysql import MysqlProcessor
import json

@api_view(['POST'])
def addDevice(request):
    request_index = request.query_params.get('index')
    # add device info
    mongodb = MongoDBProcessor()
    mysql = MysqlProcessor()
    deviceInfo = mongodb.get_camera_info(request_index)
    if mysql.add_device(deviceInfo):
        return Response('Device added', status=status.HTTP_200_OK)
    else:
        return Response('Device already exists', status=status.HTTP_409_CONFLICT)

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
        json_data = json.dumps(device_info)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse('Device not found', content_type='application/json')

@api_view(['GET'])
def GetALLDevices(request):
    # get all devices info
    db = MysqlProcessor()
    devices = db.get_all_devices()
    return Response(devices, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteDevice(request):
    request_index = request.query_params.get('index')
    # delete device info
    db = MysqlProcessor()
    if db.delete_device(request_index):
        return Response('Device deleted', status=status.HTTP_200_OK)
    else:
        return Response('Device not found', status=status.HTTP_404_NOT_FOUND)

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

@api_view(['POST', 'GET'])
def disableDevice(request):
    if request.method == 'POST':
        request_index = request.data.get('index')
        # disable device
        db = MysqlProcessor()
        if db.disable_or_enable_device(request_index):
            return Response('Status switched', status=status.HTTP_200_OK)
        else:
            return Response('Device not found', status=status.HTTP_404_NOT_FOUND)

def get_device_of_district(request):
    district = "1"
    # get device info of district
    db = MysqlProcessor()
    devices = db.get_all_devices_of_district(district)
    print(devices)
    return HttpResponse(devices)