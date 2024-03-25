#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pymongo import MongoClient

# create a MongoClient to the running mongod instance
client = MongoClient('localhost', 27017)

# get the 'smartcity' database
db = client['smartcity']

# get the 'camera' collection
camera_collection = db['camera']

# find the first document in the collection
documents = camera_collection.find()
for document in documents:
    cctv = document.get('cctv', {})
    indexes = cctv.get('index')
    print(indexes)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'camera.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
