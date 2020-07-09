# InstagramParsing
Library for Instagram parsing <br/>
You can parse:
- [x] All user information (followers , following, icon_url...)
- [x] All posts data (likes, comments, display_url...)
- [X] Parser post comments

Function for parse and sort post by likes/comments
```python
from instaparse import Post, InstaUser
from typing import (
    List, Dict, Any
)

def sort(posts: Posts = None, by: str = None) -> Posts: # sort(posts, by = 'likes')
    sort_by = 'comment_count' if by == 'comments' else 'likes_count'
    return sorted(posts, key = lambda post: post[sort_by])[::-1]
    
if __name__ == "__main__":
    account, data = InstaUser('zuck'), []
    post = Post.generate_post(account.account)

    for _ in range(account.posts_count):
        data.append(post.__next__())

    print(sort(data, by = 'comments'))
```
Function for parse all comments
```python
def parse_all_comments(account: str, data = []) -> Posts:
    for post in InstaUser(account).get_posts():
        data.append(post.get_comments())

    return data
```
Function for filter posts by date
```python
def filter_by_date(posts: Posts, _from: int,  _to: int) -> Posts:
    filter_post = [post for post in posts \
        if _from >= post['date'] >= _to]

    return filter_post
    
if __name__ == "__main__":
    account, data = InstaUser('zuck'), []
    post = Post.generate_post(account.account)

    for _ in range(account.posts_count):
        data.append(post.__next__())

    date1 = Post('https://www.instagram.com/p/CAQ6NpFA-au').date
    date2 = Post('https://www.instagram.com/p/B8rgVdbA88z').date

    print(filter_by_date(data, date1, date2))
```
You can find this functions in examples.py!
