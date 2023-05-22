#!/usr/bin/python3
"""A script to return information about
Todos list progress of employees given
their ID's
"""

import os
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise("Please enter the user Id you wish to find details about")
    url_a = 'https://jsonplaceholder.typicode.com/todos'
    url_b = 'https://jsonplaceholder.typicode.com/users'
    payload = {'userId': str(sys.argv[1])}
    try:
        req_b = requests.get(url_b)
        json_b = req_b.json()
        idx = int(sys.argv[1])
        count = 0
        completed = 0
        titles = []
        for i in json_b:
            if i.get("id") == idx:
                name = i.get("name")
        req_a = requests.get(url_a, params=payload)
        json_a = req_a.json()
        for j in json_a:
            count += 1
            if j.get("completed"):
                completed += 1
                titles.append(j.get("title"))
        print(f"Employee {name} is done with tasks({completed}/{count}):")
        [print("\t" + " " + t) for t in titles]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error!")
        print(exc_type, fname, exc_tb.tb_lineno)
