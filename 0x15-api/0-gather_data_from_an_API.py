#!/usr/bin/python3
"""
Retrieves information about an employee's TODO list progress from a REST API.
"""
import sys
import urllib.request
import json

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_url = base_url + "/users/" + str(employee_id)
    with urllib.request.urlopen(user_url) as response:
        user_data = json.loads(response.read())

    # Fetch TODOs for the user
    todos_url = f"{base_url}/todos?userId={employee_id}"
    with urllib.request.urlopen(todos_url) as response:
        todos_data = json.loads(response.read())

    # Process data and display progress
    employee_name = user_data["name"]
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")
