#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{employee_id}').json()
    todos = requests.get(f'{url}todos/?userId={employee_id}').json()

    completed = [t.get('title') for t in todos if t.get('completed') is True]
    print("Employee {} is done with tasks({:d}/{:d}:)".format(user.get('name'),
                                                              len(completed),
                                                              len(todos)))

    [print(f"\t {c}") for c in completed]
