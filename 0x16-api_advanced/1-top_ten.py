#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    limits = 10

    response = requests.get(
        apiUrl, headers={"user-agent": userAgent}, params={"limit": limits})
    if not response:
        print('None')
        return
    response = response.json()
    list_obj = response['data']['children']
    for obj in list_obj:
        print(obj['data']['title'])
    return
