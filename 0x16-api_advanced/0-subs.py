#!/usr/bin/python3
""" 
function that queries the Reddit API and returns the number of subscribers 
"""
import requests
import sys


def number_of_subscribers(subreddit):
    try:
        res = requests.get('https://www.reddit.com/r/{}/about/.json'
                           .format(sys.argv[1]),
                           headers={"User-agent": "your bot 0.1"})
        return (int(res.json().get('data').get('subscribers')))
    except:
        return (0)
