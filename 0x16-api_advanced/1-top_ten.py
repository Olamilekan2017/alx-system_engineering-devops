#!/usr/bin/python3
"""Module for interacting with the Reddit API to fetch information"""
from requests import get


URL_REDDIT = "https://www.reddit.com"
"""The API URL for Reddit"""


def top_ten(subreddit):
    """Fetches and returns titles of top ten posts from subreddit"""
    head_reddit = {
        "Accept": "application/json",
        "User-Agent": " ".join([
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
            "Firefox/124.0.2",
            "Safari/17.4.1"
        ])
    }
    resp_data = get(
        f"{URL_REDDIT}/r/{subreddit}/hot.json?limit=10",
        headers=head_reddit,
        allow_redrects=False
    )
    if resp_data.status_code == 200:
        for item_post in resp_data.json()["data"]["children"][0:10]:
            print(item_post["data"]["title"])
    else:
        print(None)
