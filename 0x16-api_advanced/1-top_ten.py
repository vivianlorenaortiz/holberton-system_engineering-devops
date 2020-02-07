#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles """

import requests
from sys import argv



def top_ten(subreddit):
    try:
        res = requests.get("https://www.reddit.com/r/{}/hot/.json?limit=10"
                           .format(subreddit),
                           headers={'User-agent': 'Holberton'},
                           allow_redirects=False)
        for i in range(0, 10):
            print(res.json().get("data").get("children")[i]
                  .get('data', {}).get('title'))
    except:
        print(None)
