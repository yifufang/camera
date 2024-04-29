from .models import Device, Incident
from django.utils import timezone
from decimal import Decimal

class MysqlProcessor:
    def __init__(self):
        pass

    def add_device(self, device_info):
        if device_info is None:
            return False
        
        if Device.objects.filter(id=device_info['id']).exists():
            return False
        else:
            device_mysql = Device(id=device_info['id'], index=device_info['index'], latitude=device_info['latitude'], longitude=device_info['longitude'], image_url=device_info['image_url'], address=device_info['address'], time=device_info['time'], district=device_info['district'], video_url=device_info['video_url'])
            device_mysql.save()
            return True
        
    def delete_device(self, id):
        if Device.objects.filter(id=id).exists():
            device_mysql = Device.objects.get(id=id)
            device_mysql.delete()
            return True
        else:
            return False
    
    def disable_or_enable_device(self, id):
        if Device.objects.filter(id=id).exists():
            device_mysql = Device.objects.get(id=id)
            device_mysql.enabled = not device_mysql.enabled
            device_mysql.save()
            return True
        else:
            return False
    
    def get_all_devices(self):
        devices = Device.objects.all().order_by('index')
        device_info = {"cameras": {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[], "10":[], "11":[], "12":[]}}
        for device in devices:
            data = {
                'id': device.id,
                'index': device.index,
                'latitude': device.latitude,
                'longitude': device.longitude,
                'address': device.address,
                'dist_id': device.district,
                'time': str(device.time),
                'status': 'active' if device.enabled else 'inactive',
                'image_url': device.image_url,
                'video_url': device.video_url
            }
            device_info["cameras"][str(device.district)].append(data)
            device_info["cameras"]["0"].append(data)
    
        return device_info
    
    #add a new incident, if theres one already, update the timestamp instead
    def add_incidents(self,lat,lon,Type):
        #lat decimal with 1 decimal place
        lat = Decimal(lat).quantize(Decimal('1.0'))
        #lon decimal with 1 decimal place
        lon = Decimal(lon).quantize(Decimal('1.0'))

    
        if Incident.objects.filter(latitude=lat,longitude=lon).exists():
            incident = Incident.objects.get(latitude=lat,longitude=lon)
            incident.timestamp = timezone.now()
            incident.save()
            return False
        else:
            incident = Incident(latitude=lat,longitude=lon,type=Type)
            incident.save()
        return True

def test():
    mysql = MysqlProcessor()
    lat = 37.7343
    lon = -122.41
    Type = 'incident'
    result = mysql.add_incidents(lat,lon,Type)
    if result:
        print('Incident added successfully')
    else:
        print('Incident already exists')

