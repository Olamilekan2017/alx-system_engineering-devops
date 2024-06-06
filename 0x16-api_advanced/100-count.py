#!/usr/bin/python3
"""Module designed for accessing the Reddit API to gather data"""
from requests import get


URL_REDDIT = "https://www.reddit.com"
"""The API URL for Reddit"""


def print_sorted_histogram(word_counts={}):
    '''Arranges and displays the histogram of word counts provided'''
    word_counts = list(filter(lambda t: t[1], word_counts))
    word_counts_dict = {}
    for item in word_counts:
        if item[0] in word_counts_dict:
            word_counts_dict[item[0]] += item[1]
        else:
            word_counts_dict[item[0]] = item[1]
    word_counts = list(word_counts_dict.items())
    word_counts.sort(
        key=lambda t: t[0],
        reverse=False
    )
    word_counts.sort(
        key=lambda t: t[1],
        reverse=True
    )
    str_result = '\n'.join(list(map(
        lambda t: '{}: {}'.format(t[0], t[1]),
        word_counts
    )))
    if str_result:
        print(str_result)


def count_words(subreddit, word_list, word_counts=[], cont=0, after=None):
    """Retrieves count of given words found in posts from subreddit"""
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
        f"{URL_REDDIT}/r/{subreddit}.json?sort={srt}&limit={lmt}"
        f"&count={cont}&after={after if after else ''}",
        headers=head_reddit,
        allow_redirects=False
    )
    if not word_counts:
        word_list = list(map(lambda word: word.lower(), word_list))
        word_counts = list(map(lambda word: (word, 0), word_list))
    if resp_data.status_code == 200:
        data = resp_data.json()['data']
        posts = data['children']
        titles = list(map(lambda post: post['data']['title'], posts))
        word_counts = list(map(
            lambda t: (t[0], t[1] + sum(list(map(
                lambda text: text.lower().split().count(t[0]),
                titles
            )))),
            word_counts
        ))
        if len(posts) >= lmt and data['after']:
            count_words(
                subreddit,
                word_list,
                word_counts,
                cont + len(posts),
                data['after']
            )
        else:
            print_sorted_histogram(word_counts)
    else:
        return
