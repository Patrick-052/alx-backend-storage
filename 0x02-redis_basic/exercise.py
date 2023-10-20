#!/usr/bin/env python3
""" A module that contains a function that stores an item in Redis. """

import redis
from uuid import uuid4
from typing import Union, Callable, Optional


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

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Takes a key string argument and an optional Callable argument
        and returns the converted data. """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Automatically parametrize Cache.get to str. """
        dstr = self._redis.get(key)
        return dstr.decode('utf-8')

    def get_int(self, key: str) -> int:
        """ Automatically parametrize Cache.get to int. """
        data = self._redis.get(key)
        try:
            dint = int(data.decode('utf-8'))
        except Exception:
            dint = 0
        return dint
