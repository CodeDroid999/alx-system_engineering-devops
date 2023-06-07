#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """Read reddit API and return top 10 hotspots """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    try:
        list_titles = r.json()['data']['children']
        while (len(hot_list) <= len(list_titles)):
            hot_list.append(len(hot_list + 1)['data']['title'])
            recurse(subreddit, hot_list)
    except:
        return("None")
