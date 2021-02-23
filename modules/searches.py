import os
import random
import requests
from json import dumps
from pathlib import Path, PurePath
from .students_model import Student


api_url = 'https://unet-api.herokuapp.com/api/v1/search/'


def process_students_data(students_data, number_of_students=10, random_data=True):
    messages_list = []
    if len(students_data) > number_of_students and random_data:
        messages_list.append(f'There are {len(students_data)} results')
        messages_list.append(
            f'Here are {number_of_students} random students')
        selection = random.sample(students_data, number_of_students)

    elif len(students_data) > 1 and not random_data:
        messages_list.append(
            f'Here are {number_of_students} some of the best results')
        selection = students_data[0:number_of_students]

    else:
        selection = students_data

    for data in selection:
        student = Student(**data)
        messages_list.append(student.show_data())

    return messages_list


def filter_data(result):
    if result['lastname'] == result['second_lastname'] or result['name'] == result['second_name']:
        return False

    return True


def search_by_expression(expression, accuracy):
    api_endpoint = f'{expression}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        max_results = 25
        results = response.json()[:max_results]
        filtered_results = list(filter(filter_data, results))
        final_data = []
        for data in filtered_results:
            if float(data['accuracy']) > float(accuracy):
                final_data.append(data)
                
        messages = process_students_data(
            final_data,
            number_of_students=len(final_data),
            random_data=False
        )

        return messages


def search_by_name(name):
    api_endpoint = f'students/name/{name}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        messages = process_students_data(response.json())
        return messages

    if response.status_code == 404:
        return {'message': 'There are not students with that name'}


def search_by_second_name(second_name):
    api_endpoint = f'students/second_name/{second_name}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        messages = process_students_data(response.json())
        return messages

    if response.status_code == 404:
        return {'message': 'There are not students with that second name'}


def search_by_lastname(lastname):
    api_endpoint = f'students/lastname/{lastname}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        messages = process_students_data(response.json())
        return messages

    if response.status_code == 404:
        return {'message': 'There are not students with that last name'}


def search_by_second_lastname(second_lastname):
    api_endpoint = f'students/second_lastname/{second_lastname}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        messages = process_students_data(response.json())
        return messages

    if response.status_code == 404:
        return {'message': 'There are not students with that second last name'}


def search_by_name_and_lastname(name, lastname):
    api_endpoint = f'students/name/{name}/lastname/{lastname}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        messages = process_students_data(response.json())
        return messages

    if response.status_code == 404:
        return {'message': 'There are not students with that name and last name'}


def search_by_dni(dni):
    api_endpoint = f'/student/dni/{dni}'
    response = requests.get(''.join([api_url, api_endpoint]))
    if response.status_code == 200:
        student = Student(**response.json())
        return student.show_data()

    if response.status_code == 404:
        return {'message': 'Dni not found'}


def search_picture(dni):
    if os.path.exists(f'./img/{dni}jpeg'):
        return open(f'./img/{dni}jpeg', 'rb')

    unet_url = f'https://control.unet.edu.ve/imagenes/FotosE/{dni}jpg'
    response = requests.get(unet_url)
    if response.status_code == 200:
        return unet_url

    if dni.startswith('V00'):
        return None

    dni = dni.replace('V', 'V00')
    return search_picture(dni)
