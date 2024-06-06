#!/usr/bin/python3
"""Module for interacting with Reddit API to obtain information"""
from requests import get


URL_REDDIT = "https://www.reddit.com"
"""The API URL for Reddit"""


def recurse(subreddit, hot_list=[], cont=0, after=None):
    """Retrieves and obtains list popular posts from subreddit"""
    head_reddit = {
            "Accept": "application/json",
            "User-Agent": " ".join([
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
                "Firefox/124.0.2",
                "Safari/17.4.1"
            ])
    }
    srt = "hot"
    lmt = 30
    resp_data = get(
        f"{URL_REDDIT}/r/{subreddit}.json?sort={srt}&limit={lmt}&"
        f"count={cont}&after={after if after else ''}",
        headers=head_reddit,
        allow_redirects=False
    )
    if resp_data.status_code == 200:
        data = resp_data.json()["data"]
        posts = data["children"]
        pst_cont = len(posts)
        hot_list.extend(list(map(lambda k: k["data"]["title"], posts)))
        if pst_cont >= lmt and data["after"]:
            return recurse(subreddit, hot_list, cont + pst_cont, data["after"])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
