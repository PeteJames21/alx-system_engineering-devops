#!/usr/bin/python3
"""
Defines a functions for getting the number of subscribers for a givem
subreddit.

Usage: ./0-subs.py SUBREDDIT
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers in the given subredit."""
    headers = {
        'User-agent': 'MyBrowser:1.0 (by /u/u/Extension_Cookie_886)'
    }
    resp = requests.get('http://www.reddit.com/r/{}/about.json'
                        .format(subreddit), headers=headers)
    try:
        resp = resp.json().get('data')
        return resp.get('subscribers', 0)
    except Exception:
        return 0
