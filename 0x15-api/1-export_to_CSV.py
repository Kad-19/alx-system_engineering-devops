#!/usr/bin/python3
'''
gather employee data from API and save to csv file
'''

import csv
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

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])
