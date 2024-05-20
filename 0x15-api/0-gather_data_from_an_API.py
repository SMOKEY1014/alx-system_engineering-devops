#!/usr/bin/python3

"""
Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import sys
import requests


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
    emp_name = user_data.get('name')

    # Fetch todos lists
    todos_responce = requests.get(todos_url)
    if todos_responce.status_code != 200:
        print('Error fetching TODO List')
        return

    todos_data = todos_responce.json()

    # Calc task statistics
    tot_tsk = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    tsk_done = len(done_tasks)

    print(f"Employee {emp_name} is done with tasks({tsk_done}/{tot_tsk}):")

    for task in done_tasks:
        print(f"\t {task['title']}")


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
