#!/usr/bin/env python3
""" web """
import requests
import redis
import functools

redis_conn = redis.Redis()


def use_cache(expiration_time):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(url):
            content = redis_conn.get(url)
            if content is not None:
                return content.decode('utf-8')

            content = func(url)
            redis_conn.setex(url, expiration_time, content)

            return content

        return wrapper
    return decorator


def count_accesses(func):
    @functools.wraps(func)
    def wrapper(url):
        key = f"count:{url}"
        redis_conn.incr(key)
        return func(url)

    return wrapper


@use_cache(expiration_time=10)
@count_accesses
def get_page(url: str) -> str:
    """ get a page with caching """
    response = requests.get(url)
    return response.text
