#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in csv file
"""

import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{employee_id}').json()
    todos = requests.get(f'{url}todos/?userId={employee_id}').json()

    csv_file = f"{employee_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        [csv_writer.writerow([employee_id,
                             user.get('username'),
                             t.get('completed'),
                             t.get('title')]) for t in todos]
