#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in JSON formate
"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{employee_id}').json()
    todos = requests.get(f'{url}todos/?userId={employee_id}').json()

    filename = f"{employee_id}.json"
    username = user.get('username')
    data = {}
    data[employee_id] = []

    for t in todos:
        employee_dict = {'task': t.get('title'),
                         'completed': t.get('completed'),
                         "username": username}

        data[employee_id].append(employee_dict)

    with open(filename, mode='w', newline='') as json_file:
        json.dump(data, json_file)
