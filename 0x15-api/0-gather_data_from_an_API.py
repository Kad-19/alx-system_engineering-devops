#!/usr/bin/python3
'''
gather employee data from API
'''

import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()

    params = {"userId": employee_id}
    tasks_response = requests.get(url + "todos", params=params)
    tasks = tasks_response.json()
    
    completed = []
    for task in tasks:
        if task.get("completed") is True:
            completed.append(task.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"), len(completed), len(tasks)))

    for title in completed:
        print("\t {}".format(title))
