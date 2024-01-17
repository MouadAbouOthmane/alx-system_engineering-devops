#!/usr/bin/python3
""" 1. Top Ten """


def top_ten(subreddit):
    """ Reddit API endpoint for getting the hot posts of a subreddit"""
    import requests

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'test'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children'][:10]

            if not posts:
                print("None")
                return

            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print(None)
    except Exception as e:
        print(None)
