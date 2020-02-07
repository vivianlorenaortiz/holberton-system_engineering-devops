 #!/usr/bin/python3
""" function that queries the Reddit API and prints the titles """

import requests
from sys import argv


def top_ten(subreddit):
    """
    """
    try:
        url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                             .format(subreddit),
                             headers={'User-agent': 'vivianortiz'},
                             allow_redirects=False).json()

        for top in url.get('data').get('children'):
            print(top.get('data').get('title'))
    except Exception:
        print(None)
