from .models import Device

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
