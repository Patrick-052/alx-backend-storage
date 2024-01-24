#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ Decorator counting how many times
    a URL is accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text

# #!/usr/bin/env python3
# """ Module that contains implementation of scraping
#     and returning the results """

# import redis
# import requests
# from functools import wraps
# from typing import Callable

# r = redis.Redis()


# def count_requests(get_page: Callable[[str], str]) -> Callable[[str], str]:
#     """ Count the number a request is made """

#     @wraps(get_page)
#     def wrapper(url):
#         """ wrapper function to count the number
#         of requests with key count as an expiry key """
#         cached = f"cached:{url}"
#         if r.get(cached):
#             return r.get(cached).decode('utf-8')

#         count = f"count:{url}"
#         page = get_page(url)

#         r.incr(count)
#         r.setex(cached, 10, page)
#         return page

#     return wrapper


# @count_requests
# def get_page(url: str) -> str:
#     """ Function that returns the HTML content of a URL """
#     res = requests.get(url)
#     return res.text
