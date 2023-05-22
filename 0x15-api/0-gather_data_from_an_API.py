#!/usr/bin/python3
"""
Returns TODO list progress for a given employee ID.
"""

import sys
import requests


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        completed_tasks = [task.get("title") for task in todos_data if task.get("completed")]

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task_title in completed_tasks:
            print(f"\t {task_title}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
