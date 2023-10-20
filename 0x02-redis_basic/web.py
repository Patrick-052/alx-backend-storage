#!/usr/bin/env python3
""" Module that contains implementation of scraping
    and returning the results """

import requests
import redis
from functools import wraps
from typing import Callable


def count_requests(method: Callable) -> Callable:
    """ Count the number a request is made """

    @wraps(method)
    def wrapper(url):
        """ wrapper function to count the number
        of requests with key count as an expiry key """
        r = redis.Redis()
        count = f"count:{url}"
        r.incr(count)
        r.expire(count, 10)
        return method(url)

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Function that returns the HTML content of a URL """
    req = requests.get(url)
    return req.text
