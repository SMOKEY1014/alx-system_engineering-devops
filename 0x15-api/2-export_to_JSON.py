#!/usr/bin/python3

"""
Python script to export data in the JSON format.
"""

import requests
import sys
import json


def fetch_employee_data(employee_id):
    # API endpoints
    emp_id = employee_id
    td = "todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/{td}"

    user_responce = requests.get(user_url)
    if user_responce.status_code != 200:
        print('Error fetching user data')
        return

    user_data = user_responce.json()
    username = user_data.get('username')

    # Fetch todos lists
    todos_responce = requests.get(todos_url)
    if todos_responce.status_code != 200:
        print('Error fetching TODO List')
        return

    todos_data = todos_responce.json()
    exp_to_json(emp_id, username, todos_data)


def exp_to_json(emp_id, username, todos_data):
    filename = f"{employee_id}.json"

    task_list = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
            }
        for task in todos_data
        ]
    data = {str(emp_id): task_list}

    with open(filename, mode='w') as file:
        json.dump(data, file)

    # with open(filename, mode='w', encoding='utf8') as file:
    #     json.dump(data, file, indent=4)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 <python-script.py> <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an interger")
        sys.exit(1)

    fetch_employee_data(employee_id)
