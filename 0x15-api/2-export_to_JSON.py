#!/usr/bi/python3
"""
Dictionary of list of dictionaries
"""

import json
import requests
from sys import argv

def export_json(user_id):
    """
    Export to JSON
    """
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()

    username = user.get('username')
    all_task = []
    for task  in todo:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('complete')
        task_dict['username'] = username
        all_task.append(task_dict)
    json_task = {}
    json_task[user_id] = all_task
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(json_task, jsonfile)

if __name__ == "__main__":
     export_json(int(argv[1]))
