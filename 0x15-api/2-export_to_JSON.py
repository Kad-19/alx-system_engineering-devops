#!/usr/bin/python3
'''
gather employee data from API and save to json file
'''

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()

    username = user.get("username")

    params = {"userId": employee_id}
    tasks_response = requests.get(url + "todos", params=params)
    tasks = tasks_response.json()

    json_data = {employee_id: []}

    for task in tasks:
        task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
        }
        json_data[employee_id].append(task_info)

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
