#!/usr/bin/python3
"""
0-subs.py
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    subscribers = 0
    if subreddit:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        res = requests.get(url, allow_redirects=False)
        if res.status_code == 200:
            subreddit_about = res.json()
            subscribers = subreddit_about.get('data').get('subscribers')
    return subscribers
