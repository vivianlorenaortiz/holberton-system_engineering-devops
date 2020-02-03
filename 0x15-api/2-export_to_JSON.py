#!/usr/bin/python3

""" Dictionary of list of dictionaries """

import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id)).json()
    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
