#!/usr/bin/python3
"""
2-recurse.py
"""
import requests


def recurse(subreddit, hot_list=[], i=0, posts=[]):
    """
    returns a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    if i == 0:
        if subreddit is None:
            return None
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        headers = {
        'User-agent': 'ubuntu 20.04'
        }
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return None
        posts = res.json().get('data').get('children')
    if i == len(posts):
        return hot_list
    hot_list.append(posts[i].get('data').get('title'))
    recurse(subreddit, hot_list, i + 1, posts)
    return hot_list
