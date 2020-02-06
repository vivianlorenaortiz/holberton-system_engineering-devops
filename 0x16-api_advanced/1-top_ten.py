#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles """
import requests
from sys import argv


def top_ten(subreddit):
    """
    """
    user = {'User-Agent': 'vivianOrtiz'}
    title = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                         .format(subreddit), headers=user).json()
    try:
        for top in url.get('data').get('children'):
            print(top.get('data').get('title'))
    except Exception:
        print(None)
