from pymongo import MongoClient
from django.utils import timezone

class MongoDBProcessor:
    def __init__(self):
        #mongoDB connection
        self.client = MongoClient('mongodb://adminUser:adminPassword@54.177.184.253:27017/')
        self.db = self.client['smartcity']
        self.camera_collection = self.db['camera']

    # get device info   
    def get_camera_info(self, index):
        camera_info = self.camera_collection.find_one({'cctv.index': index})
        latitude = camera_info['cctv']['location']['latitude']
        longitude = camera_info['cctv']['location']['longitude']
        index = camera_info['cctv']['index']
        image_url = camera_info['cctv']['imageData']['static']['currentImageURL']
        address = camera_info['cctv']['location']['locationName']
        district = camera_info['cctv']['location']['district']
        time = timezone.now()

        return {'latitude': latitude, 'longitude': longitude, 'index': index, 'image_url': image_url, 'address': address, 'time':time ,'district': district}

    def get_image_url(self, index):
        camera_info = self.camera_collection.find_one({'cctv.index': index})
        image_url = camera_info['cctv']['imageData']['static']['currentImageURL']
        return image_url
    
    