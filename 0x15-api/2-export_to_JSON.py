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
        current = {}
        current["task"] = task.get('title')
        current["completed"] = task.get('completed')
        current["username"] = username
        tasks.append(current)
    json_task = {}
    json_task[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(json_task, jsonfile)
