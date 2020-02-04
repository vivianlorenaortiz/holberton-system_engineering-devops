#!/usr/bin/python3
""" Dictionary of list of dictionaries """

import json
import requests


if __name__ == '__main__':

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    userdict = {}
    current_user = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        current_user[uid] = user.get("username")

        for task in todo:
            current_dict = {}
            uid = task.get("user_id")
            current_dict["task"] = task.get('title')
            current_dict["completed"] = task.get('completed')
            current_dict["username"] = current_user.get(uid)
            userdict.get("uid").append(current_dict)

    with open(filaname, 'w') as jsonfile:
        json.dump(dict_user, jsonfile)
