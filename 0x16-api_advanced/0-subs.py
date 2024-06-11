#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.

Requirements:
Prototype: def number_of_subscribers(subreddit)
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number 
    of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = 'User Agent'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data')
        if data and data.get('display_name') == subreddit:
            return data.get('subscribers', 0)
        else:
            return 0
    else:
        return 0
