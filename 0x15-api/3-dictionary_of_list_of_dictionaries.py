#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in JSON formate
"""

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + '/users/').json()

    filename = "todo_all_employees.json"
    data = {}

    for user in users:
        username = user.get('username')
        id = user.get('id')
        todos = requests.get(f"{url}/todos/?userId={id}").json()
        print(todos)
        data[id] = []
        for t in todos:
            employee_dict = {'username': username,
                             'task': t.get('title'),
                             'completed': t.get('completed')}

            data[id].append(employee_dict)

    with open(filename, mode='w', newline='') as json_file:
        json.dump(data, json_file)
