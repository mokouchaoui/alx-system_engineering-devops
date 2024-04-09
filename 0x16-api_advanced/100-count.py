#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords.
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """
    Add title to list.
    """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """
    queries the Reddit API.
    """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """
    Init count.
    """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    lo = sorted(dictionary.items(), key=lambda kv: kv[1])
    lo.reverse()

    if len(lo) != 0:
        for item in lo:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
