#!/usr/bin/python3
"""
Defines a function that prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return a list of the titles of the top 10 hot posts for a given subreddit.

    "None" is returned if the subreddit is invalid
    """
    headers = {
        'User-Agent': 'MyBrowser:1.0 (by /u/Extension_Cookie_886)'
    }
    sub = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=headers)

    try:
        sub = sub.json().get('data')
        after = sub.get('after', None)
        if not after:
            raise Exception
        sub = sub.get('children')
        for obj in sub:
            hot_list.append(obj['data'].get('title'))
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
