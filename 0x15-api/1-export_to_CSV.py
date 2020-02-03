#!/usr/bin/python3
'''
    Export a JSON
'''
import csv
import requests
from sys import argv


if __name__ == "__main__":

    userid = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userid)).json()
    All = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(userid)).json()
    N = user.get('name')
    filename = userid + '.csv'
    with open(filename, 'w', newline='') as csv_file:
        tasks = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in All:
            tasks.writerow([userid, user.get('username'),
                            task.get('completed'), task.get('title')])


if __name__ == "__main__":
