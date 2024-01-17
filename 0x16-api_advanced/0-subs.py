#!/usr/bin/python3
"""0. How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """Reddit API endpoint for getting subreddit information"""
    if not subreddit:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'intranet test'}

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
    except Exception as e:
        return 0
