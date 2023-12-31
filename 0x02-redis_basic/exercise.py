#!/usr/bin/env python3
""" A module that contains a function that stores an item in Redis. """

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """ Storing method's args in a list and returning
        the args from an output list
        Process:
           - Retrieve method name
           - Append args to a redis list
           - Return list of arg's values from redis db """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """ wrapper function to store method args in a list
        and return the arg's values in a list """
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Count the number of times a method is called.
        Process:
           - Retrieve method name
           - Increment key's value everytime called using (.incr())
           - Return value of method called (call it)
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper func to increment method count in
        redis db and return it. """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def replay(method: Callable) -> None:
    """ Displaying history of calls of a particular function
        Process:
           - Retrieve method name
           - Retrieve method count from redis db (key count)
           - Retrieve method inputs and outputs from redis db
           - Print out the history of calls
    """
    r = redis.Redis()
    key = method.__qualname__
    count = r.get(key).decode('utf-8')
    inputs = r.lrange(f"{key}:inputs", 0, -1)
    outputs = r.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {count} times:")
    zipped = zip(inputs, outputs)
    for i, o in zipped:
        print(f"{key}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache:
    """ Implementing a Cache class. """

    def __init__(self):
        """ Initialize. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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


if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
