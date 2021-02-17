import requests
from .students_model import Student


url_api = 'https://unet-api.herokuapp.com/api/v1/search/'


def search_by_dni(dni):
    dni_endpoint = f'/student/dni/{dni}'
    response = requests.get(''.join([url_api, dni_endpoint]))
    if response.status_code == 200:
        student = Student(**response.json())
        
        return student