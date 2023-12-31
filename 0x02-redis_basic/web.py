#!/usr/bin/env python3
""" Module that contains implementation of scraping
    and returning the results """

import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(get_page: Callable[[str], str]) -> Callable[[str], str]:
    """ Count the number a request is made """

    @wraps(get_page)
    def wrapper(url):
        """ wrapper function to count the number
        of requests with key count as an expiry key """
        cached = f"cached:{url}"
        if r.get(cached):
            return r.get(cached).decode('utf-8')

        count = f"count:{url}"
        page = get_page(url)

        r.incr(count)
        r.setex(cached, 10, page)
        return page

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Function that returns the HTML content of a URL """
    res = requests.get(url)
    return res.text
