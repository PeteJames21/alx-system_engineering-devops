#!/usr/bin/python3
"""
Defines a function that prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the top 10 hot posts for a given subreddit.

    "None" is printed if the subreddit is invalid
    """
    headers = {
        'User-agent': 'MyBrowser:1.0 (by /u/Extension_Cookie_886)'
    }
    resp = requests.get('http://www.reddit.com/r/{}/hot.json'
                        .format(subreddit), headers=headers,
                        allow_redirects=False)

    try:
        resp = resp.json().get('data')
        resp = resp.get('children', None)
        if not resp:
            raise Exception
        i = 0
        for obj in resp:
            if i > 9:
                break
            print(obj['data'].get('title'))
            i += 1

    except Exception:
        print('None')
