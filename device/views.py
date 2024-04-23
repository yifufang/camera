from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .mongodb import MongoDBProcessor
from .mysql import MysqlProcessor
import json

@api_view(['POST'])
def addDevice(request):
    request_id = int(request.query_params.get('id'))
    # add device info
    mongodb = MongoDBProcessor()
    mysql = MysqlProcessor()
    deviceInfo = mongodb.get_camera_info(request_id)
    if mysql.add_device(deviceInfo):
        return Response('Device added', status=status.HTTP_200_OK)
    else:
        return Response('Device already exists', status=status.HTTP_409_CONFLICT)

@api_view(['GET'])
def GetALLDevices(request):
    # get all devices info
    db = MysqlProcessor()
    devices = db.get_all_devices()
    return Response(devices, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteDevice(request):
    request_id = request.query_params.get('id')
    # delete device info
    db = MysqlProcessor()
    if db.delete_device(request_id):
        return Response('Device deleted', status=status.HTTP_200_OK)
    else:
        return Response('Device not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['POST', 'GET'])
def disableDevice(request):
    request_id = request.query_params.get('id')
    # disable device
    db = MysqlProcessor()
    if db.disable_or_enable_device(request_id):
        return Response('Status switched', status=status.HTTP_200_OK)
    else:
        return Response('Device not found', status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def searchedDevice(request):
    search_term = request.query_params.get('search')
    # search device
    db = MongoDBProcessor()
    result = db.search_device(search_term)
    return Response(result, status=status.HTTP_200_OK)
