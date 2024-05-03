## Introduction
before you start this:
1. you need to have .env configured to set environment informations
2. you need to have cuda installed and configure let pytorch use your gpu
3. you need to have ffmpeg installed and add to path

then run this project run:

    pip install requirements.txt
    python manage.py runserver

## API Docs
| Description                                                      | API Path                      | Request Type | Parameter                            |
|------------------------------------------------------------------|-------------------------------|--------------|--------------------------------------|
| Get one active device information from database                  | /api/AddDevice/?id            | GET          | Device index                         |
| Remove a active device                                           | /api/DeleteDevice/?id         | DELETE       | Device index                         |
| Get all devices currently active                                 | /api/GetAllDevices            | GET          | n/a                                  |
| Disable a device                                                 | /api/DisableDevice/?id        | GET          | Device index                         |
| Search a device by their index, address, location                | /api/SearchDevice/?search     | GET          | search term                          |
| AI detection streaming                                           | /api/StreamVideo/?url&latitude&longitude&district     | GET          | Device Index                         |
| Get all the incidences detected by AI                            | /api/GetAllIncidences/        | GET          | n/a                                  |
| stop camera streaming                                            | /api/StopStream/              | GET          | n/a                                  |
