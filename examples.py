from instaparse import Post, InstaUser
from datetime import datetime, date

from typing import (
    List, Dict, Any
)

Posts = List[Dict[str, str]]

def sort(posts: Posts = None, by: str = None) -> Posts: # sort(posts, by = 'likes')
    sort_by = 'comment_count' if by == 'comments' else 'likes_count'
    return sorted(posts, key = lambda post: post[sort_by])[::-1]

def post_generator(posts: Posts) -> Post:
    for post in posts:
        yield post

def parse_all_comments_author(account: str, data = []) -> List[str]:
    for post in InstaUser(account()).get_posts():
        comments = post.get_comments()
        for comment in comments:
            if not comment['owner'] in data:
                data.append(comment['owner'])

    return data

def parse_all_comments(account: str, data = []) -> Posts:
    for post in InstaUser(account).get_posts():
        data.append(post.get_comments())

    return data

def filter_by_date(posts: Posts, _from: int,  _to: int) -> Posts:
    filter_post = [post for post in posts \
        if _from >= post['date'] >= _to]

    return filter_post
