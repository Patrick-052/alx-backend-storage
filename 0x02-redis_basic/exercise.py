#!/usr/bin/env python3
""" A module that contains a function that stores an item in Redis. """

import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Implementing a Cache class. """

    def __init__(self):
        """ Initialize. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes a data argument and returns a string. """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
