#!/usr/bin/python3

""" Dictionary of list of dictionaries """

import json
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()

    name = user.get('username')
    file_name = user_id + 'json'
    all_task = []
    for task in todo:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = name
        all_task.append(task_dict)
    json_task = {}
    json_task[user_id] = all_task
    with open(file_name, 'w') as jsonfile:
        json.dump(json_task, jsonfile)
