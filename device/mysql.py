from .models import Device

class MysqlProcessor:
    def __init__(self):
        pass

    def add_device(self, device_info):
        if Device.objects.filter(index=device_info['index']).exists():
            return False
        else:
            device_mysql = Device(index=device_info['index'], latitude=device_info['latitude'], longitude=device_info['longitude'], image_url=device_info['image_url'], address=device_info['address'], time=device_info['time'], district=device_info['district'])
            device_mysql.save()

    def update_device_info(self, device_info):
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
            device_mysql = Device(index=device_info['index'], latitude=device_info['latitude'], longitude=device_info['longitude'], image_url=device_info['image_url'], address=device_info['address'], time=device_info['time'], district=device_info['district'])
            device_mysql.save()

    def get_device_info(self, request_index):
        if Device.objects.filter(index=request_index).exists():
            device_mysql = Device.objects.get(index=request_index)
            device_info = {
                'latitude': device_mysql.latitude,
                'longitude': device_mysql.longitude,
                'image_url': device_mysql.image_url,
                'address': device_mysql.address,
                'district': device_mysql.district,
                'time': device_mysql.time
            }
            return device_info
        else:
            return None
        
    def delete_device(self, request_index):
        if Device.objects.filter(index=request_index).exists():
            device_mysql = Device.objects.get(index=request_index)
            device_mysql.delete()
            return True
        else:
            return False
    
    def updateImage(self, request_index, image_url):
        if Device.objects.filter(index=request_index).exists():
            device_mysql = Device.objects.get(index=request_index)
            device_mysql.image_url = image_url
            device_mysql.save()
            return True
        else:
            return False
    
    def disable_device(self, request_index):
        if Device.objects.filter(index=request_index).exists():
            device_mysql = Device.objects.get(index=request_index)
            device_mysql.enabled = False
            device_mysql.save()
            return True
        else:
            return False
    
    def get_all_devices_of_district(self, district):
        devices = Device.objects.filter(district=district)
        device_info = []
        for device in devices:
            device_info.append({
                'latitude': device.latitude,
                'longitude': device.longitude,
                'image_url': device.image_url,
                'address': device.address,
                'district': device.district,
                'time': device.time
            })
        return device_info
    