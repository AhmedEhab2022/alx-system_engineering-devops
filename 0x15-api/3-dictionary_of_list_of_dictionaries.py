#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in JSON formate
"""

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/').json()
    all_todos = requests.get(f'{url}todos/').json()

    filename = "todo_all_employees.json"
    data = {}

    for user in users:
        username = user.get('username')
        id = user.get('id')
        for tod in all_todos:
            employee_id = tod.get('userId')
            todos = requests.get('{url}todos/?userId={employee_id}').json()
            for t in todos:
                data[employee_id] = []
                employee_dict = {
                                    'username': username,
                                    'task': t.get('title'),
                                    'completed': t.get('completed'),
                                }

                data[employee_id].append(employee_dict)

    with open(filename, mode='w', newline='') as json_file:
        json.dump(data, json_file)
