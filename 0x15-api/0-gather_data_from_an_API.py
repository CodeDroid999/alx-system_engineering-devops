#!/usr/bin/python3
"""
Gathers data from an API for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_url = base_url + "users/{}".format(user_id)
    todos_url = base_url + "todos?userId={}".format(user_id)

    user_response = requests.get(user_url, verify=False).json()
    todos_response = requests.get(todos_url, verify=False).json()

    print("Employee {} is done with tasks {}/{}:".format(
        user_response["name"],
        sum(1 for todo in todos_response if todo["completed"]),
        len(todos_response)
    ))

    for todo in todos_response:
        if todo["completed"]:
            print("\t{}".format(todo["title"]))
