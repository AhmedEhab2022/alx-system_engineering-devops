#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
     listed for a given subreddit.
     """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    res = requests.get(url, allow_redirects=False)
    if res.status_code == 200:
        subreddit_posts = res.json().get('data').get('children')
        for i in range(10):
            print(subreddit_posts[i].get('data').get('title'))
    else:
        print(None)
