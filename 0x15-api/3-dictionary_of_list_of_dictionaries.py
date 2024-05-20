#!/usr/bin/python3

"""
Python script to export data in the JSON format.
"""

import requests
import json


def fetch_employees_data():
    # API endpoints
    td = "todos"
    users_url = f"https://jsonplaceholder.typicode.com/users"
    todos_url = f"https://jsonplaceholder.typicode.com/{td}"

    users_responce = requests.get(users_url)
    if users_responce.status_code != 200:
        print('Error fetching users data')
        return

    users_data = users_responce.json()

    # Fetch todos lists
    todos_responce = requests.get(todos_url)
    if todos_responce.status_code != 200:
        print('Error fetching TODO List')
        return
    todos_data = todos_responce.json()

    # Organize data to required format
    all_tasks = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos_data if task['userId'] == user_id]

        task_list = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
                }
            for task in user_tasks
        ]
        all_tasks[user_id] = task_list

    exp_to_json(all_tasks)


def exp_to_json(data):
    filename = "todo_all_employees.json"

    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    fetch_employees_data()
